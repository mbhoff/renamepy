#!/usr/bin/env python3

# ***** cmdargparse.py *****
# Python script to parse command-line arguments using argparse module.
# CSC461 Programming Languages, Fall 2016 (JMW)
# Usage: python cmdargparse.py [-h] [-v] [-i N] [-f N] x y [n1 n2 n3 ...]
# Prints x**y and [n1,n2,...]

import sys, argparse, glob, os, fnmatch
from functions import *



if __name__ == '__main__':

    parser = argparse.ArgumentParser( usage = "-h for help, -v for verbose, -i for int, -f for float" )

    # optional switches (may occur in any order)
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
    parser.add_argument("-t", "--trim", type=int,metavar="N", help="positive n: trim n chars from the start of each filename negative n: trim n chars from the end of each filename")
    #parser.add_argument("-f", "--real", type=float, metavar="N", help="supply a float value")
    parser.add_argument("-l", "--lower", action="store_true", help="converts filename to lowercase")
    parser.add_argument("-u", "--upper", action="store_true", help="converts filename to uppercase")
    parser.add_argument("-p", "--print", action="store_true", help="prints the old and new filenames without rewriting them")
    parser.add_argument("-i", "--interactive", action="store_true", help="turns on interactive mode")
    parser.add_argument("-r", "--replace", type=str, nargs=2, metavar=("oldfilename", "newfilename"), help="replaces the oldfilename with the new filename")
    parser.add_argument("-n", "--number", type=str,metavar="N", help="rename files in sequence using count string #'s in count string become numbers")
    parser.add_argument("-d", "--delete", action="store_true", help="deletes the file")
    parser.add_argument("-dt", "--touch", action="store_true", help="updates time stamps to current time")
    parser.add_argument("-D", "--date", type=int, metavar="DDMMYYYY",help="updates the date time stamps to specified date")
    parser.add_argument("-T", "--time", type=int, metavar="HHMMSS", help="updates the time stamps to specified date")



    # required positional arguments
    '''
    parser.add_argument("x", type=int, help="base")
    parser.add_argument("y", type=int, help="exponent")
    '''
    # followed by 0 or more strings
    parser.add_argument("names", type=str, nargs='+', help="list of strings")

    # parse command arguments
    args = parser.parse_args()
    # print results of parsing
    #print( args.x, "**", args.y, "=", args.x ** args.y )
    '''print( 'cmd args:', sys.argv )
    print( 'argparse:', args )
    print( 'args.verbose =', args.verbose )
    print( 'args.lower =', args.lower )
    print( "names: ", args.names )
    '''
    
    #print("test")
    originalFileNames = [];
    for s in args.names:
        for filename in glob.glob(s):
            originalFileNames.append(filename)
    #print(originalFileNames)
    newFileNames = originalFileNames[:]
    
    if args.delete:
        delete(originalFileNames,args.interactive)
    else:
        curIndex = 0;
        for curArg in sys.argv:
            if curArg in ('-l','--lower'):
                for i in range(len(newFileNames)):
                    if args.verbose:
                        print('file:',newFileNames[i],end=' ')            
                    newFileNames[i] = lower(newFileNames[i], args.interactive)
                    if args.verbose:
                        print('was changed to',newFileNames[i])
            elif curArg in ('-u','--upper'):
                for i in range(len(newFileNames)):
                    if args.verbose:
                        print('file:',newFileNames[i],end=' ')  
                    newFileNames[i] = upper(newFileNames[i], args.interactive)
                    if args.verbose:
                        print('was changed to',newFileNames[i])

            elif curArg in ('-t','--trim'):
                for i in range(len(newFileNames)):
                    if args.verbose:
                        print('file:',newFileNames[i],end=' ')
                    newFileNames[i] = trim(newFileNames[i],int(sys.argv[curIndex+1]), args.interactive)
                    if args.verbose:
                        print('was changed to',newFileNames[i])

            elif curArg in ('-r','--replace'):
                for i in range(len(newFileNames)):
                    if args.verbose:
                        print('file:',newFileNames[i],end=' ')  
                    newFileNames[i] = replaceReg(newFileNames[i],sys.argv[curIndex+1], sys.argv[curIndex+2], args.interactive)
                    if args.verbose:
                        print('was changed to',newFileNames[i])
            
            
            elif curArg in ('-n','--number'):
                for i in range(len(newFileNames)):
                    if args.verbose:
                        print('file:',newFileNames[i],end=' ')  
                    newFileNames[i] = countString(sys.argv[curIndex+1],i+1, args.interactive)
                    if args.verbose:
                        print('was changed to',newFileNames[i])

            elif curArg in ('-dt','--touch'):
                touch(originalFileNames,args.interactive)

            elif curArg in ('-D','--date'):
                date(originalFileNames,args.date,args.interactive)


            elif curArg in ('-T','--time'):
                time(originalFileNames,args.time,args.interactive)
            
            curIndex += 1

        if args.print:
            oldNew(originalFileNames, newFileNames)
        else:
            changename(originalFileNames, newFileNames)

