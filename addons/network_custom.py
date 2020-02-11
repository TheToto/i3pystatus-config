import netifaces
from fnmatch import fnmatch

from i3pystatus import network


class NetworkCustom(network.Network):
    on_middleclick = "nm-connection-editor"
    on_leftclick = "networkmanager_dmenu"

    def cycle_interface(self, increment=1):
        """Cycle through available interfaces in `increment` steps. Sign indicates direction."""
        interfaces = []
        for i in netifaces.interfaces():
            for pattern in self.ignore_interfaces:
                if fnmatch(i, pattern):
                    break
            else:
                interfaces.append(i)

        if self.interface in interfaces:
            next_index = (interfaces.index(self.interface) + increment) % len(
                interfaces
            )
            self.interface = interfaces[next_index]
        elif len(interfaces) > 0:
            self.interface = interfaces[0]

        if self.network_traffic:
            self.network_traffic.clear_counters()
            self.kbs_arr = [0.0] * self.graph_width
