#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler





def save_file(filename, show_run):
    """Save the show run to a file"""
    with open(filename, "w") as f:
        f.write(show_run)

rtr1 = {
        'device_type': 'cisco_ios',
        'ip':   '184.105.247.70',
        'username': 'pyclass',
        'password': '88newclass',
    }

sw1 = {
        'device_type': 'arista_eos',
        'ip':   '184.105.247.72',
        'username': 'admin1',
        'password': '99saturday',
    }


def connect_net_device(**kwarg):
    net_connect = ConnectHandler(**kwarg)
    print "Current prompt: {}".format(net_connect.find_prompt())
    show_run = net_connect.send_command("sh run")
    print "sh run output: \n\n{}".format(show_run)
    filename = net_connect.base_prompt + ".txt"
    save_file (filename , show_run)
    
def main():
    connect_net_device(**rtr1)
    connect_net_device(**sw1)

if __name__ == "__main__":
    main()
