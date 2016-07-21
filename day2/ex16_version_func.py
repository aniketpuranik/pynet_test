#!usr/bin/env python


def get_file(file_name):

    with open(file_name) as f:
        show_ver = f.read().splitlines()
    return show_ver

def print_serial(file_output):
    sn = 'Processor board ID'
    for line in file_output:
        if sn in line:
            print line
            serial_number = line.split("Processor board ID")
            return serial_number[1]

file_output = get_file("sh-ver")
serial_number = print_serial(file_output)

print file_output
print "serial number : {}".format(serial_number)
