#!/usr/bin/env python3

#Import Moudls

import os
import sys
from socket import *
import time
from Moudls import Iplocation, Portscaner, Host_ip
from help import help

def IClear():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")


#------------
try:
    import ipapi
    from colorama import Fore
    import requests
except:
    Interface()
    print("")
    print("Please Install requirments file\n")
#-------------
while True:



    try:
        help.Banner()
        help.infolist1()
        print("")
        number = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Cruppy"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ").lower()
    except:
        print("\n Gos Lock :)")
        sys.exit()
    if number == "":
        print(Fore.RED+"Gode By :(")
    elif number == "5":
        IClear()
        print(Fore.RED+'Gode Lock :(')
        sys.exit()
    elif number == "4":
        IClear()
        help.Banner()
    elif number == "3":
        IClear()
        help.Banner()
        Iplocation.__start__()
    elif number == "2":
        IClear()
        help.Banner()
        Host_ip.__start__()
    elif number == "1":
        IClear()
        help.Banner()
        Portscaner.__start__()
