#TODO Ask if we need to preserve file extensions
import sys

def checkYes(a):
    return a in ('yes','y')

def verbose():
    print("verbose")
def trim():
    print("trim")
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
def oldNew():
    print("print")
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
