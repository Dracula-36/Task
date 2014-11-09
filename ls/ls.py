#!/usr/bin/python3
#Filename:ls.py
def show(a):
    import glob
    if a==1:
        files=glob.glob("*")+glob.glob(".*")
        print('.')
        print('..')
    else:
        files=glob.glob("*")
    for i in files:
        print(i)
def showR(a,s):
    import os
    import glob
    if a ==1:
        files=glob.glob("*")+glob.glob(".*")
    else:
        files=glob.glob("*")
    if s==1:
        print(os.getcwd(),':')
        s=0
    show(a)
    for i in files:
        if os.path.isdir(i):
            os.chdir(i)
            print(os.getcwd(),':')
            showR(a,s)
    os.chdir("..")
    return
import os
import sys
if len(sys.argv)!=1:
    if ('/' in sys.argv[-1])or('~' in sys.argv[-1]):
        os.chdir(sys.argv[-1])
        if ('-aR' in sys.argv)or('-Ra' in sys.argv)or(('-a' in sys.argv)and('-R' in sys.argv)):
            showR(1,1)
        elif ('-R' in sys.argv):
            showR(0,1)
        elif ('-a' in sys.argv):
            show(1)
        else:
            show(0)
    else:
        if ('-aR' in sys.argv)or('-Ra' in sys.argv)or(('-a' in sys.argv)and('-R' in sys.argv)):
            showR(1,1)
        elif ('-R' in sys.argv):
            showR(0,1)
        elif ('-a' in sys.argv):
            show(1)
        else:
            show(0)
else:
    show(0)





