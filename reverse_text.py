#!/bin/python

import sys
import argparse

def main():
    try:
        with open (sys.argv[1], 'r') as my_file:
        #setting file read of 1st argv to first variable
            v1 = (my_file.read())
        #Check to make sure the file was being taken as a variable, left in for debugging??
        #print(v1)

            v2 = v1.split()
            v2.reverse()
            result = " ".join(v2)

            print(result[::-1])

    except:
        print ("Yo. Maybe try the -h switch. Just a thought. Who am I, I just made the thing....")

parser=argparse.ArgumentParser(
    description='''Tool to reverse words in Spector Ops Challenge 1 ''',
    epilog="""All's well that ends well.""")

parser.add_argument('FILEPATH', nargs='*', default=[1, 2, 3], help='File to Read! and Reverse!')
args=parser.parse_args()

main()
