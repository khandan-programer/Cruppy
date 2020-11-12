from socket import *
from colorama import Fore
import sys

def __start__():
    print('')
    print('')
    print(Fore.RED+"["+Fore.WHITE+"卐"+Fore.RED+"]"+Fore.CYAN+"Please Enter a Domain")
    print('')
    print('')
    Domain = input((Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Cruppy"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Host To IP"+Fore.RED+"""]
    └──╼ """+Fore.WHITE+"卐 "))
    ip_Finder = socket(AF_INET , SOCK_STREAM)
    ip = gethostbyname(Domain)
    print('')
    print('')
    print(Fore.RED+"["+Fore.WHITE+"Cruppy"+Fore.RED+"]"+Fore.GREEN+" IP Address Founded")
    print('')
    print('')
    print(Fore.CYAN+'IP Address => '+Fore.GREEN+ip)
    print('')
    print('')
    input(Fore.RED+"Back To Menue (Prees Enter)")
