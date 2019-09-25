#!/usr/bin/env python3
''' This is housekeeping.py
version 0.01 '''

import os
import getpass
# add crypto

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# clear the screen
cls()

p = getpass.getpass(prompt='Password: ', stream=None)

def housework():   
    a = os.getcwd()
    print(a)
    path = "C:\\"
    print(path)

    if a != path:
        os.chdir( path )
    print(path)

    if os.path.exists("testfile.txt"):
        os.remove("testfile.txt")
        print("File removed.")
    else:
        print("The file does not exist")

# change to crypto
if p == 'lnxdork':
    print("right")
else:
    print("nope")
    housework()