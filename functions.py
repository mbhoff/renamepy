#TODO Ask if we need to preserve file extensions
import sys, os, datetime, time, re

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
def delete(inNames,interactive):
    for filename in inNames:
        good = True
        if interactive:
            qStr = 'do you want to delete ' + filename + '?(y/n): '
            good = checkYes( input(qStr) )
        if good:
            os.remove(filename)
def touch(inNames,interactive):
    for filename in inNames:
        good = True
        if interactive:
            qStr = 'do you want to touch ' + filename + '?(y/n): '
            good = checkYes( input(qStr) )
        if good:
            ct = datetime.datetime.now()
            os.utime(filename,(ct.timestamp(), ct.timestamp()))

def date(inNames, dat ,interactive):
    for filename in inNames:
        good = True
        if interactive:
            qStr = 'do you want to change date for file ' + filename + '?(y/n): '
            good = checkYes( input(qStr) )
        if good:
            ot = os.path.getmtime(filename)
            odt = datetime.datetime.fromtimestamp(ot)
            nt = datetime.datetime(dat % 10000, (dat // 10000) % 100, (dat // 1000000) % 100,odt.hour,odt.minute,odt.second)
            os.utime(filename,(nt.timestamp(), nt.timestamp()))
def time(inNames, tim ,interactive):
    for filename in inNames:
        good = True
        if interactive:
            qStr = 'do you want to change time for ' + filename + '?(y/n): '
            good = checkYes( input(qStr) )
        if good:
            ot = os.path.getmtime(filename)
            odt = datetime.datetime.fromtimestamp(ot)
            nt = datetime.datetime(odt.year,odt.month,odt.day,(tim //10000) % 100,(tim // 100) % 100,tim % 100)
            os.utime(filename,(nt.timestamp(), nt.timestamp()))

def replaceReg(filename,reg1,reg2, interactive):
    good = True
    if interactive:
        qStr = 'do you want to use the supplied regex expression to replace ' + reg1 + " with " + reg2 + " for file named:" + filename + '?(y/n): '
        good = checkYes( input(qStr) )
    if good:
        return re.sub((reg1),(reg2),filename)
    else:
        return filename

def countString(filename,index, interactive):
    good = True
    if interactive:
        qStr = 'do you want to rename file in sequence for file named:' + filename + '?(y/n): '
        good = checkYes( input(qStr) )
    if good:
        filename = filename[::-1]
        while filename.rfind('#') != -1:
            filename = filename.replace('#', str(index % 10), 1)
            index = index // 10
        return filename[::-1]
    else:
        return filename


