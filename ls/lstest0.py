#!/usr/bin/python3
def show():
    import glob
    filename=glob.glob("*")+glob.glob(".*")
    for name in filename:
       print(name)
def lsR():
    import glob
    import os
    show()
    filename=glob.glob("*")+glob.glob(".*")
    for name in filename:
        if os.path.isdir(name):
            os.chdir(name)
            print(os.getcwd(),':')
            lsR()
    os.chdir("..")
    return
lsR()
