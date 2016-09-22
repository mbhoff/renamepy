#TODO Ask if we need to preserve file extensions
import sys, os, datetime, time, re

def checkYes(a):
    """Checsks to see if yes or a variation of yes was provided. Returns true or false"""
    return a in ('yes','y')


def trim(filename, n, interactive):
    """Trims the input name by the number given.
    Positive number starts from start
    Negative numbers start from the end"""
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
    """Converts the filename to lowercase"""
    good = True
    if interactive:
        qStr = 'do you want to LowerCase ' + filename + '?(y/n): '
        good = checkYes( input(qStr) )
    if good:
        return filename.lower()
    else:
        return filename
def upper(filename, interactive):
    """Converts the filename to UpperCase"""
    good = True
    if interactive:
        qStr = 'do you want to UpperCase ' + filename + '?(y/n): '
        good = checkYes( input(qStr) )
    if good:
        return filename.upper()
    else:
        return filename
def changename(originalFileNames, newFileNames):
    """Replaces old filenames with new filenames"""
    for i in range(len(newFileNames)):
        os.rename(originalFileNames[i], newFileNames[i])
def oldNew(oldFileNames,newFileNames):
    """Prints out the names of the old file and the new name it would have been given"""
    for i in range(len(oldFileNames)):
        print('Original File Name:',oldFileNames[i],'New File Name:',newFileNames[i])
def delete(inNames,interactive):
    """Deletes files that match the names given"""
    for filename in inNames:
        good = True
        if interactive:
            qStr = 'do you want to delete ' + filename + '?(y/n): '
            good = checkYes( input(qStr) )
        if good:
            os.remove(filename)
def touch(inNames,interactive):
    """Updtates the modified date and time to current date and time"""
    for filename in inNames:
        good = True
        if interactive:
            qStr = 'do you want to touch ' + filename + '?(y/n): '
            good = checkYes( input(qStr) )
        if good:
            ct = datetime.datetime.now()
            os.utime(filename,(ct.timestamp(), ct.timestamp()))

def date(inNames, dat ,interactive):
    """Changes modified date to the given date"""
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
    """Changes the modified time to the given time"""
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
    """Changes the given name using the provided regular expressions"""
    good = True
    if interactive:
        qStr = 'do you want to use the supplied regex expression to replace ' + reg1 + " with " + reg2 + " for file named:" + filename + '?(y/n): '
        good = checkYes( input(qStr) )
    if good:
        return re.sub((reg1),(reg2),filename)
    else:
        return filename

def countString(filename,index, interactive):
    """Replaces the # symbomols in the given filename with the number given""" 
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


