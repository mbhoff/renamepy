import glob
import argparse
import os
import stat
import datetime

parser = argparse.ArgumentParser( usage = "-h for help, -v for verbose, -i for int, -f for float" )

# optional switches (may occur in any order)
parser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
parser.add_argument("-i", "--integer", type=int, metavar="N", help="supply an int value")
parser.add_argument("-f", "--real", type=float, metavar="N", help="supply a float value")



args = parser.parse_args()
print(args.accumulate(args.integers))


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

