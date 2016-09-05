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
parser.add_argument("-i", "--integer", type=int, metavar="N", help="supply an int value")
parser.add_argument("-f", "--real", type=float, metavar="N", help="supply a float value")

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
print( 'args.integer =', args.integer )
print( 'args.real =', args.real )
print( args.x, "**", args.y, "=", args.x ** args.y )
print( "names: ", args.names )


if __name__ == '__main__':
    print("test")


