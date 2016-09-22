#!/usr/bin/env python3

# ***** cmdargparse.py *****
# Python script to parse command-line arguments using argparse module.
# CSC461 Programming Languages, Fall 2016 (JMW)
# Authors: Mark Buttenhoff and Micah Picasso
# Usage: python3 rename.py [-l] [-u] [-t N] [-r oldstring newstring] [-n count string] [-h] [-v] [-p] [-i] [-d] [-dt] [-D DDMMYYYY] [-T HHMMSS] file1 file2 ...
# Modified from cmdargparse.py provided by Dr. Weiss for CSC461 Fall 2016


import sys, argparse, glob, os, fnmatch
from functions import *


#used to simulate main
if __name__ == '__main__':
    #parser for parsing the given arguments
    parser = argparse.ArgumentParser( usage = "-h for help, -v for verbose, -i for int, -f for float" )

    # optional switches (may occur in any order)
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
    parser.add_argument("-t", "--trim", type=int,metavar="N", help="positive n: trim n chars from the start of each filename negative n: trim n chars from the end of each filename")
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


    # followed by 0 or more strings
    parser.add_argument("names", type=str, nargs='+', help="list of strings")

    # parse command arguments
    args = parser.parse_args()

    
    #make empty list to store file names
    originalFileNames = [];
    
    #get all the file names into the originalFilesNames list
    for s in args.names:
        for filename in glob.glob(s):
            originalFileNames.append(filename)

    #copy file names to new list
    newFileNames = originalFileNames[:]
    
    #if delete is called all other ooptions are ignored
    if args.delete:
        delete(originalFileNames,args.interactive)
    #all other arguments
    else:
        curIndex = 0;
        #check each argument
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
        #print new file names instead of renaming
        if args.print:
            oldNew(originalFileNames, newFileNames)
        #rename files
        else:
            changename(originalFileNames, newFileNames)

