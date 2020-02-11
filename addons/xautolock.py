from i3pystatus import Module
from i3pystatus.core.command import execute


class Xautolock(Module):
    settings = ()
    on_leftclick = "toggle"
    on_rightclick = on_leftclick
    on_middleclick = on_leftclick

    def init(self):
        self.activated = True
        self.update_output()

    def update_output(self):
        self.output = {
            "full_text": "",
            "color": "#ffffff" if self.activated else "#ff0000"
        }

    def toggle(self):
        if self.activated:
            execute("xautolock -disable")
        else:
            execute("xautolock -enable")
        self.activated = not self.activated
        self.update_output()
