#!/usr/bin/env python

import django
from net_system.models import Credentials
from net_system.models import NetworkDevice

net_devices = NetworkDevice.objects.all()
print net_devices

all_creds = Credentials.objects.all()
print all_creds

std_cred = all_creds[0]
arista_cred = all_creds[1]

for a_device in net_devices:
     if a_device.device_type == 'cisco_ios':
         a_device.credentials = std_cred
     else:
         a_device.credentials = arista_cred
     a_device.save()
     print a_device.credentials

a_device.credentials = std_cred
a_device.save()


for a_device in net_devices:
    a_device.save()
    netmiko_device = {}
    netmiko_device{device_type} = a_device.device_type
    netmiko_device{ip_address} = a_device.ip_address
    netmiko_device{uername} = a_device.credentials.username
    netmiko_device{password} = a_device.credentials.password
    connect_net_device(**netmiko_device)



def connect_net_device(**kwarg):
    net_connect = ConnectHandler(**kwarg)
#    print "Current prompt: {}".format(net_connect.find_prompt())
    show_arp = net_connect.send_command("sh arp")
    print "sh run output: \n\n{}".format(show_arp)
    filename = net_connect.base_prompt + ".txt"
    #save_file (filename , show_run)
