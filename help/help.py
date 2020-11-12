from colorama import Fore
import sys
import os
import time

print("")

def Banner():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    print(Fore.LIGHTRED_EX, '''

  ██████╗██████╗ ██╗   ██╗██████╗ ██████╗ ██╗   ██╗
 ██╔════╝██╔══██╗██║   ██║██╔══██╗██╔══██╗╚██╗ ██╔╝
 ██║     ██████╔╝██║   ██║██████╔╝██████╔╝ ╚████╔╝
 ██║     ██╔══██╗██║   ██║██╔═══╝ ██╔═══╝   ╚██╔╝
 ╚██████╗██║  ██║╚██████╔╝██║     ██║        ██║
  ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝        ╚═╝
===================================================
**                                               **
**         Coded by Mohamad Sobhan Khandan       **
**                                               **
===================================================
''')

def infolist1():
    time.sleep(0.2)
    print("")
    print(Fore.RED+"["+Fore.WHITE+"卐"+Fore.RED+"]"+Fore.CYAN+" Please Choose an Option ")
    print("")
    print(Fore.RED+"["+Fore.WHITE+"1"+Fore.RED+"]"+Fore.BLUE+" Port Scanner")
    print("")
    print(Fore.RED+"["+Fore.WHITE+"2"+Fore.RED+"]"+Fore.GREEN+" Host To IP")
    print("")
    print(Fore.RED+"["+Fore.WHITE+"3"+Fore.RED+"]"+Fore.RED+" Ip Location")
    print("")
    print(Fore.RED+"["+Fore.WHITE+"4"+Fore.RED+"]"+Fore.YELLOW+" Developer :)")
    print("")
    print(Fore.RED+"["+Fore.WHITE+"5"+Fore.RED+"]"+Fore.GREEN+" exit .....")
