#!/bin/python

import sys
import argparse


def main():

    try:
        #setting file read of 1st argv to first variable
        with open (sys.argv[1], 'r') as my_file:

            v1 = (my_file.read())

        #Check to make sure the file was being taken as a variable, left in for debugging?
        #print(v1)
            mystring = v1.strip('\n')

            d = {}
        # count occurances of character
            for w in mystring:
                d[w] = mystring.count(w)
        # print the result
            for k in sorted(d):
                print (k + ': ' + str(d[k]))

    except:
        print ("Yo. Maybe try the -h switch. Just a thought. Who am I, I just made the thing....")




parser=argparse.ArgumentParser(
    description='''Tool to locate frequency of characters in given file input at first argument. ''',
    epilog="""All's well that ends well.""")

parser.add_argument('FILEPATH', nargs='*', default=[1, 2, 3], help='File to Read and Analyze Character Frequency of, ex: Specter2.py FILEPATH')
args=parser.parse_args()


main()
