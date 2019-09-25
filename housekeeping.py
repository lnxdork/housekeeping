#!/usr/bin/env python3
''' This is housekeeping.py
version 0.02 '''

import os
import getpass
import signal
import time
from pbkdf2 import crypt

starttime=time.time()
timeout = 30

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

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

def interrupted(signum, frame):
    "called when read times out"
    print('interrupted!')
    housework()
    exit()
signal.signal(signal.SIGALRM, interrupted)

# clear the screen
while True:
    cls()
    pwhash = "$p5k2$$l8MU49Wf$DnF1ouSnIN55uak18OY6rG11faMdmIhh"
    signal.alarm(timeout)
    p = getpass.getpass(prompt='Password: ', stream=None)

    if pwhash == crypt(p, pwhash):
        print("Password accepted, sleeping...")
        signal.alarm(0)
        time.sleep(60.0 * 15)
    else:
        print("Invalid password")
        housework()
        exit()