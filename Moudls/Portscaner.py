from socket import *
import sys
import time
from colorama import Fore

print("")

def __start__():
    print ("")
    print ("")
    print(Fore.LIGHTBLACK_EX+"\n [!] Simple Port Scanner ! ! !")
    print(Fore.MAGENTA+"\n [!] Plase Enter IP/Domain\n")
    print("")
    ip = input((Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Cruppy"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Port-Scan"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 "))
    ipn = gethostbyname(ip)
    print('')
    print('')
    print("Scan Stared => "+ipn)
    print('')
    print('')
    try:
        for i in range(1 , 9000):
            s = socket(AF_INET , SOCK_STREAM)
            result = s.connect_ex((ipn , i))
            if (result == 0):
                print(Fore.GREEN+"Port %d: is Open" %(i, ))
    except:
        print(Fore.RED+"Gode by :(")
        sys.exit()
    try:
        input(Fore.RED, "back To Menu (Press Enter ...")
    except:
        print("")
        sys.exit()
