#!/usr/bin/env python
from netmiko import ConnectHandler
import yaml
from pprint import pprint
#filename=''

#with open('rtr1.yml') as f:
    #my_rtr1 = yaml.load(f)


def connect_net_device(**kwargs):
    net_connect = ConnectHandler(**kwargs)
    sh_arp = net_connect.send_command("sh arp")
    print(sh_arp)

def main():

    with open('rtr1.yml') as f:
        my_rtr1 = yaml.load(f)
    my_rtr1 = my_rtr1['rtr1']
    connect_net_device(**my_rtr1)

    print type(my_rtr1)
    print my_rtr1

if __name__ == "__main__":
    main()
