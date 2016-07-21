#!usr/bin/env python
from pprint import pprint
import re
import sys

def get_file(file_name):
    with open(file_name) as f:
        return f.read()



class ShVer(object):

    def __init__(self,file_output):
        self.file_output = file_output
        self.serial = ''
        self.vendor = ''
        self.uptime = ''
        self.version = ''
        self.model = ''        

    def print_serial(self):
        match = re.search(r"^Processor .* (FTX.*)", self.file_output, flags=re.M)
        if match:
        #return match.group(1)
            self.serial = match.group(1)

    def print_vendor(self):
        match = re.search(r"^Copyright .* (Cisco.*).*", self.file_output, flags=re.M)
        if match:
        #return match.group(1)
            self.vendor = match.group(1)

    def print_uptime(self):
        match = re.search(r"uptime .* (3 weeks.*)", self.file_output, flags=re.M)
        if match:
        #return match.group(1)
            self.uptime = match.group(1)

    def print_version(self):
        match = re.search(r"^Cisco .* (Version.*),", self.file_output, flags=re.M)
        if match:
        #return match.group(1)
            self.version = match.group(1)

    def print_model(self):
        match = re.search(r"^Cisco 881", self.file_output, flags=re.M)
        if match:
        #return match.group(1)
            self.model = match.group(0)



def main():
    file_output = get_file("sh-ver")
    
    net_dev_obj = ShVer(file_output)
    net_dev_obj.print_serial()
    net_dev_obj.print_vendor()
    net_dev_obj.print_uptime()
    net_dev_obj.print_version()
    net_dev_obj.print_model()
    
    
    print "Serial  number: {}".format(net_dev_obj.serial)
    print "Vendor  name  : {}".format(net_dev_obj.vendor)
    print "Uptime        : {}".format(net_dev_obj.uptime)
    print "Version number: {}".format(net_dev_obj.version)
    print "Model   number: {}".format(net_dev_obj.model)

if __name__ == "__main__":
    main()
