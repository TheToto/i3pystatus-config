import glob

from i3pystatus.core.command import run_through_shell
from i3pystatus.file import File


class Rfkill(File):
    settings = (
        (
            "format",
            "format string, formatters: name, hard, soft, type, index, hard_bool, soft_bool",
        ),
        (
            "rfkill",
            "rfkill, see `/sys/class/rfkill/`. Supports glob expansion, i.e. `*` matches anything. "
            "If it matches more than one filename, selects the first one in alphabetical order",
        ),
        ("rfkill_name", "Name of rfkill device"),
        "color",
        "down_color",
    )
    required = ()

    down_color = "#FF0000"

    rfkill = "*"
    rfkill_name = None
    base_path = "/sys/class/rfkill/{rfkill}/"
    components = {
        "name": (str, "name"),
        "hard": (int, "hard"),
        "soft": (int, "soft"),
        "type": (str, "type"),
        "index": (int, "index"),
    }
    transforms = {
        "hard_bool": lambda cdict: cdict["hard"] == 1,
        "soft_bool": lambda cdict: cdict["soft"] == 1,
    }

    format = "{name} {soft}/{hard}"

    on_leftclick = "rfkill_switch"
    on_rightclick = on_leftclick

    def abort(self):
        self.run = self.run_no_rfkill
        super().init()

    def init(self):
        self.base_path = self.base_path.format(rfkill=self.rfkill)
        rfkill_entries = sorted(glob.glob(self.base_path))

        if len(rfkill_entries) == 0:
            return self.abort()

        if self.rfkill_name:
            for entry in rfkill_entries:
                self.base_path = entry
                self.run()
                if self.data["name"] == self.rfkill_name:
                    break
            else:
                return self.abort()
        else:
            self.base_path = rfkill_entries[0]

        super().init()

    def run_no_rfkill(self):
        if self.rfkill_name:
            self.output["full_text"] = f"No rfkill device : {self.rfkill_name}"
        else:
            self.output["full_text"] = "No rfkill device"

    def run(self):
        super().run()
        if self.data["hard_bool"] or self.data["soft_bool"]:
            self.output["color"] = self.down_color

    def rfkill_switch(self):
        run_through_shell(
            [
                "rfkill",
                "unblock" if self.data["soft_bool"] else "block",
                str(self.data["index"]),
            ]
        )
