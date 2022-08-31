import subprocess
import time

from colorama import Fore, Back, Style


ilk_yazi = "Gerekli Toollar Indirilmeye başlıyor ..."

print(Fore.LIGHTRED_EX+ilk_yazi)

time.sleep(2)

subprocess.call(["sudo","pacman","-S","nmap"])

time.sleep(1)

subprocess.call(["sudo","pacman","-S","dnsutils"])

son_yazi = "Indirme başariyla tamamlandi, Terminali kapatabilirsiniz ! "

print(Fore.LIGHTCYAN_EX+son_yazi)


