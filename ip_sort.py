#!/bin/python3

import sys
import argparse
import ipaddress

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

def main():
    try:
        #setting file read of 1st argv to first variable
        with open (sys.argv[1], 'r') as my_file:

            ips = sorted(set(ipaddress.ip_address(line.strip()) for line in my_file))
            print('\n'.join(map(str, ips)))

    except:
        print ("Yo. Maybe try the -h switch. Just a thought. Who am I, I just made the thing....")

    parser=argparse.ArgumentParser(
    description='''List unique IP Addresses for Spector Ops Challenge 3 ''',
    epilog="""All's well that ends well.""")

    parser.add_argument('FILEPATH', nargs='*', default=[1, 2, 3], help='File to read and list IP addresses ')
    args=parser.parse_args()

main()
