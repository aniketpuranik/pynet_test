#!/usr/bin/env python
from pprint import pprint
import pyeapi

pynet_sw1 = pyeapi.connect_to("pynet-sw2")
sh_ip_route = pynet_sw1.enable("show ip route")
output = sh_ip_route[0]
output = output['result']['vrfs']['default']
routes = output['routes']
pprint(routes)
print type(routes)


print "\n{:>15} {:>15} {:>15}".format("prefix", "interface", "next_hop")
filler = "-" * 15
print "{:>15} {:>15} {:>15}".format(filler, filler, filler)
for prefix, attr in routes.items():
    intf_nexthop = attr['vias'][0]
    pprint(intf_nexthop)
    interface = intf_nexthop.get('interface', 'N/A')
    next_hop = intf_nexthop.get('nexthopAddr', 'N/A')
    print "{:>15} {:>15} {:>15}".format(prefix, interface, next_hop)
print
