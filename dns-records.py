#!/usr/bin/env python
__author__ = 'meder'

import sys
import csv

# listFile should be a CSV list of hostnames
try:
    list_file = sys.argv[1]
except:
    print("You must supply a list of hostnames in CSV format")


def make_commands(file):
    #   Read given csv file
    list = csv.reader(file)
    for host, ip in list:
        print("Generating commands for %s" % host)
        a_record = 'echo -e "update delete %s. IN A %s \\nsend\\n" | nsupdate -l -k /etc/named/rndc.key' % (host,ip)
        txt_record = 'echo -e "update delete %s. IN TXT %s \\nsend\\n" | nsupdate -l -k /etc/named/rndc.key' % (host,ip)
        ptr_record = 'echo -e "update delete %s.in-addr.arpa \\nsend\\n" | nsupdate -l -k /etc/named/rndc.key' % (ip)
        cname_record = 'echo -e "update delete %s \\nsend\\n" | nsupdate -l -k /etc/named/rndc.key' % (host)
        da_record = 'echo -e "update delete %s IN A %s \\nsend\\n" | nsupdate -l -k /etc/named/rndc.key' % (ip,ip)
        print(a_record)
        print(txt_record)
        print(ptr_record)
        print(cname_record)
        print(da_record)
        print('\n')

if __name__ == "__main__":
    with open(list_file, "rb") as file:
        make_commands(file)
