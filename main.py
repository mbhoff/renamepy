#!/usr/bin/env python3

# ***** cmdargparse.py *****
# Python script to parse command-line arguments using argparse module.
# CSC461 Programming Languages, Fall 2016 (JMW)
# Usage: python cmdargparse.py [-h] [-v] [-i N] [-f N] x y [n1 n2 n3 ...]
# Prints x**y and [n1,n2,...]

import sys, argparse


parser = argparse.ArgumentParser( usage = "-h for help, -v for verbose, -i for int, -f for float" )

# optional switches (may occur in any order)
parser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
parser.add_argument("-t", "--trim", type=int, metavar="N", help="trims the filename a certain number of digits from the beginning")
#parser.add_argument("-f", "--real", type=float, metavar="N", help="supply a float value")
parser.add_argument("-l", "--lower", action="store_true", help="converts filename to lowercase")
parser.add_argument("-u", "--uppper", action="store_true", help="converts filename to uppercase")
parser.add_argument("-p", "--print", action="store_true", help="prints the old and new filenames without rewriting them")
parser.add_argument("-i", "--interactive", action="store_true", help="turns on interactive mode")
parser.add_argument("-r", "--replace", type=str, nargs=2, metavar=("oldfilename", "newfilename"), help="replaces the oldfilename with the new filename")
parser.add_argument("-d", "--delete", action="store_true", help="deletes the file")
parser.add_argument("-dt", "--touch", action="store_true", help="updates time stamps to current time")
parser.add_argument("-D", "--date", type=int, metavar="N", help="updates the date time stamps to specified date")
parser.add_argument("-T", "--time", type=int, metavar="N", help="updates the time stamps to specified date")



# required positional arguments
parser.add_argument("x", type=int, help="base")
parser.add_argument("y", type=int, help="exponent")

# followed by 0 or more strings
parser.add_argument("names", type=str, nargs='*', help="list of strings")

# parse command arguments
args = parser.parse_args()

# print results of parsing
print( 'cmd args:', sys.argv )
print( 'argparse:', args )
print( 'args.verbose =', args.verbose )
print( 'args.lower =', args.lower )
print( args.x, "**", args.y, "=", args.x ** args.y )
print( "names: ", args.names )


if __name__ == '__main__':
    print("test")


