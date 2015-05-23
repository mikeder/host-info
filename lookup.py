#!/usr/bin/env python
__author__ = 'meder'

import socket
import sys
import csv

# listFile should be a CSV list of hostnames
try:
    list_file = sys.argv[1]
except:
    print("You must supply a list of hostnames in CSV format")


def lookup_dns(file):
    #   Read given csv file
    list = csv.reader(file)
    for host in list:
        print("Looking up %s" % host[0])
        try:
            ip = socket.gethostbyname(host[0])
            host.append(ip)
            print("IP: {0}").format(host[1])
            csv_writer(host)
        except Exception as err:
            print("Error while looking up DNS for %s" % host[0])
            print(err)

def csv_writer(line):
    with open('output.csv', 'a+') as list_out:
        writer = csv.writer(list_out, delimiter=',')
        writer.writerow(line)

if __name__ == "__main__":
    with open(list_file, "rb") as file:
        lookup_dns(file)
