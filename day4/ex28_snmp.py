#!/usr/bin/env python
from getpass import getpass
from snmp_helper import snmp_get_oid_v3, snmp_extract

ifDescr = '1.3.6.1.2.1.2.2.1.2.7'
inOctets = '1.3.6.1.2.1.2.2.1.10.7'
outOctets = '1.3.6.1.2.1.2.2.1.16.7'

my_key = getpass(prompt = 'Enter auth key and encryption key: ')

py_user = 'pysnmp'
auth_key = my_key
encrypt_key = my_key

snmp_user = (py_user, auth_key, encrypt_key)
rtr1 = ('184.105.247.70', 161)

print auth_key

print"\n {:<15} {:<15} {:<15}".format('ifDescr','inOctets','outOctets')

results = []

for oid in (ifDescr, inOctets, outOctets):
    snmp_data = snmp_get_oid_v3(rtr1, snmp_user, oid = oid)
#    print snmp_data
    results.append(snmp_extract(snmp_data))
    print results
    #break
#print "{:>15} {:>15} {:>15}".format(*results)
print

