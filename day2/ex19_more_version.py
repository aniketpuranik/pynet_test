#!usr/bin/env python
from pprint import pprint

def get_file(file_name):

    with open(file_name) as f:
        return f.read().splitlines()


def print_serial(file_output):
    sn = 'Processor board ID'
    for line in file_output:
        if sn in line:
   #         print line
            serial_number = line.split("Processor board ID")
            return serial_number[1]

def get_vendor(file_output):
    sn = 'Copyright (c) 1986-2014 by'
    for line in file_output:
        if sn in line:
    #        print line
            vendor = line.split(sn)
            return vendor[1]


def get_uptime(file_output):
    sn = 'pynet-rtr1 uptime is'
    for line in file_output:
        if sn in line:
  #          print line
            uptime = line.split(sn)
            return uptime[1]


def get_version(file_output):
    sn = 'Cisco IOS Software, C880 Software'
    for line in file_output:
        if sn in line:
 #           print line
            version = line.split(",")
            return version[2]


def get_model(file_output):
    sn = 'Cisco 881'
    for line in file_output:
        if sn in line:
#            print line
            model = line.split(" ")
            return model[0]+" "+model[1]



file_output = get_file("sh-ver")

switch_info = {}

switch_info['serial_number'] = print_serial(file_output)
switch_info['vendor'] = get_vendor(file_output)
switch_info['uptime'] = get_uptime(file_output)
switch_info['version'] = get_version(file_output)
switch_info['model'] = get_model(file_output)

# k,v in switch_info.items():
print (switch_info)

#print file_output
#print "serial number : {}".format(serial_number)
#print "vendor        : {}".format(vendor)
#print "uptime        : {}".format(uptime)
#print "version       : {}".format(version)
#print "model         : {}".format(model)





