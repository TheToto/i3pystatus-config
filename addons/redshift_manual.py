from i3pystatus import formatp
from i3pystatus import redshift


class RedshiftManual(redshift.Redshift):
    settings = (
        ("color", "Text color"),
        "format",
        ("step", "Steps in K for mouse scroll"),
        ("redshift_parameters", "List of parameters to pass to redshift binary"),
    )

    format = "{temperature}K"
    step = 200

    interval = 60 * 60

    on_leftclick = "auto_value"
    on_rightclick = "reset_value"
    on_downscroll = "decrease"
    on_upscroll = "increase"

    def run_redshft(self, args):
        self._controller = redshift.RedshiftController(self.redshift_parameters + args)
        self._controller.start()
        self._controller.join()
        self.update_values()

    def auto_value(self):
        self.run_redshft(["-P", "-o"])

    def reset_value(self):
        self.run_redshft(["-x"])
        self.temperature = 6500

    def increase(self):
        if self.temperature - self.step > 25000:
            self.temperature = 25000 - self.step
        self.run_redshft(["-P", "-O", str(self.temperature + self.step)])

    def decrease(self):
        if self.temperature - self.step < 1000:
            self.temperature = 1000 + self.step
        self.run_redshft(["-P", "-O", str(self.temperature - self.step)])

    def init(self):
        self.temperature = 6500

    def run(self):
        fdict = {
            "temperature": self.temperature,
        }
        output = formatp(self.format, **fdict)
        color = self.color

        self.output = {
            "full_text": output,
            "color": color,
        }
