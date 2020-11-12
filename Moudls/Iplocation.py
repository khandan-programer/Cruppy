import requests
import os
import sys
from colorama import Fore
from socket import *
import webbrowser
import urllib3
import  time

def __start__():
    print("")
    print("")
    print(Fore.YELLOW+"["+Fore.WHITE+"卐"+Fore.YELLOW+"]"+Fore.CYAN+"Please Enter ip Address")
    print("")
    print('')
    Domain = input((Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Cruppy"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Ip Location"+Fore.RED+"""]
    └──╼ """+Fore.WHITE+"卐 "))
    #ip = int(Domain)
    http = urllib3.PoolManager()
    Location = http.request('GET', 'http://api.hackertarget.com/geoip/?q='+Domain)
    print("")
    print('')
    print(Fore.LIGHTYELLOW_EX+"["+Fore.WHITE+"Cruppy"+Fore.LIGHTYELLOW_EX+"]"+Fore.GREEN+" -> ip Adrees Found")
    print("")
    print("")
    print(Location.data)
    input(Fore.RED+"Back To Menue (Prees Enter)")
