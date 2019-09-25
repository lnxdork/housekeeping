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
    file_name = "testfile.txt"
    print(path)

    if a != path:
        os.chdir( path )
    print(path)
    
    if os.path.exists(file_name):
        f = open(file_name,'wb')
        f.write(b'0101010101010101') # make data passes
        f.close
        os.rename(file_name, "0000000000") # make rename passes
        os.remove("0000000000")
        print("File removed.")
    else:
        print("The file does not exist")

pwhash = "$p5k2$$l8MU49Wf$DnF1ouSnIN55uak18OY6rG11faMdmIhh"

if pwhash == crypt(p, pwhash):
    print("Password good")
else:
    print("Invalid password")
    housework()