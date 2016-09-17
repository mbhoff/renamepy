#TODO Ask if we need to preserve file extensions
import sys, os

def checkYes(a):
    return a in ('yes','y')


def trim(filename, n, interactive):
    good = True
    if interactive:
        qStr = 'do you want to trim ' + n + ' characters from ' + filename + '?(y/n): '
        good = checkYes( input(qStr) )
    if good:
        if n > 0:
            return filename[n:len(filename)]
        else:
            return filename[0:len(filename)+n]
    else:
        return filename

def lower(filename, interactive):
    good = True
    if interactive:
        qStr = 'do you want to LowerCase ' + filename + '?(y/n): '
        good = checkYes( input(qStr) )
    if good:
        return filename.lower()
    else:
        return filename
def upper(filename, interactive):
    good = True
    if interactive:
        qStr = 'do you want to UpperCase ' + filename + '?(y/n): '
        good = checkYes( input(qStr) )
    if good:
        return filename.upper()
    else:
        return filename
def changename(originalFileNames, newFileNames):
    for i in range(len(newFileNames)):
        os.rename(originalFileNames[i], newFileNames[i])
def oldNew(oldFileNames,newFileNames):
    for i in range(len(oldFileNames)):
        print('Original File Name:',oldFileNames[i],'New File Name:',newFileNames[i])
def replace():
    print("replace")
def delete():
    print("delete")
def touch():
    print("touch")
def date():
    print("date")
def time():
    print("time")
