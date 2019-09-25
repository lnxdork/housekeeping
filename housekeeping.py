#!/usr/bin/env python3
''' This is housekeeping.py
version 0.01 '''

import os
import getpass
from pbkdf2 import crypt

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# clear the screen
cls()

p = getpass.getpass(prompt='Password: ', stream=None)

def housework():   
    a = os.getcwd()
    print(a)
    path = "/home/lnxdork/"
    print(path)

    if a != path:
        os.chdir( path )
    print(path)

    if os.path.exists("testfile.txt"):
        os.remove("testfile.txt")
        print("File removed.")
    else:
        print("The file does not exist")

pwhash = "$p5k2$$l8MU49Wf$DnF1ouSnIN55uak18OY6rG11faMdmIhh"

if pwhash == crypt(p, pwhash):
    print("Password good")
else:
    print("Invalid password")
    housework()