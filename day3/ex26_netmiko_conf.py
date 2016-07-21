#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler


sw1 = {
        'device_type': 'arista_eos',
        'ip':   '184.105.247.72',
        'username': 'admin1',
        'password': '99saturday',
    }


def connect_net_device(**kwarg):
    net_connect = ConnectHandler(**kwarg)
    print "Current device: {}".format(net_connect.find_prompt())
