#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse


def main():
    cisco_file = 'pynet-rtr1.txt'
    cisco_cfg = CiscoConfParse(cisco_file)
    interfaces = cisco_cfg.find_objects(r"^interface")
    for interface in interfaces:
        print
        print interface.text
        for child in interface.children:
            print child.text
    print

    interfacess = cisco_cfg.find_objects_w_child(parentspec=r'interface',
                                                 childspec=r'no ip address')
    print "\nInterfaces without ip address:"
    for interface in interfaces:
        print "  {0}".format(interface.text)
    print

#    crypto_maps = cisco_cfg.find_objects_wo_child(parentspec=r'crypto map CRYPTO',
#                                                  childspec=r'set peer 5.5.5.1')
#    print "\nCrypto maps not peer 5.5.5.1:"
#    for entry in crypto_maps:
#        print "  {0}".format(entry.text)
#    print

if __name__ == "__main__":
    main()
