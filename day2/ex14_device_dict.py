#!/usr/bin/env python

network_device = {
 'ip_addr'    : '81.1.1.3',
 'username'   : 'user1',
 'passwd'     : 'pass123',
 'vendor'     : 'cisco',
 'model'      : '3940',

}

for k,v in network_device.items():
    print k,v

network_device['passwd']='newpass'
network_device['secret']='enable'

for k,v in network_device.items():
    print k,v


device_type = network_device.get('device_type', 'cisco_ios')
print "\nDefault device type: {}\n".format(device_type)
