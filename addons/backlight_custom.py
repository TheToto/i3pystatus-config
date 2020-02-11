from i3pystatus import backlight
from i3pystatus.core.command import run_through_shell


class BacklightCustom(backlight.Backlight):
    def lighter(self):
        run_through_shell(["light", "-A", "2"])

    def darker(self):
        run_through_shell(["light", "-U", "2"])
