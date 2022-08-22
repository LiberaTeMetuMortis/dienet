from multiprocessing.resource_sharer import stop
import requests
import time
import subprocess
import colorama
from colorama import Fore, Back, Style
dienet = """
 ________  ___  _______   ________   _______  _________   
|\   ___ \|\  \|\  ___ \ |\   ___  \|\  ___ \|\___   ___\ 
\ \  \_|\ \ \  \ \   __/|\ \  \\ \  \ \   __/\|___ \  \_| 
 \ \  \ \\ \ \  \ \  \_|/_\ \  \\ \  \ \  \_|/__  \ \  \  
  \ \  \_\\ \ \  \ \  \_|\ \ \  \\ \  \ \  \_|\ \  \ \  \ 
   \ \_______\ \__\ \_______\ \__\\ \__\ \_______\  \ \__\\
    \|_______|\|__|\|_______|\|__| \|__|\|_______|   \|__|
                                                          
"""
print(Fore.LIGHTCYAN_EX+dienet)
giris_ekran = int(input("""                                                                                                     
[1]Kaynak kodu getir    [2]Header Bilgi al

[3]HTTP durum al        [4]encode degeri al

[5]Nmap taramasi al     [6]Ip bilgisi al
**********************************************************
"""))

if giris_ekran == 1:
    url = input("Url'yi giriniz : ")
    source_code = requests.get(url)
    print(source_code.text)

elif giris_ekran == 2:
    url = input("Url'yi giriniz :")
    header = requests.get(url)
    print(header.headers)

elif giris_ekran == 3:
    url = input("Url'yi giriniz : ")
    status = requests.get(url,allow_redirects=True)
    print(status.history)

elif giris_ekran == 4:
    url = input("Url'yi giriniz : ")
    encode = requests.get(url, timeout=2)
    print(encode.encoding)

elif giris_ekran == 5:
    url = input("Url'yi giriniz(https olmadan orn. dsociety.cf) : ")
    subprocess.call(["nslookup",url])
    time.sleep(3)
    ip = input("Taranicak ip'i giriniz : ")
    subprocess.call(["nmap","-A","-vv",ip])

elif giris_ekran == 6:
    url = input("Url'yi giriniz(https olmadan orn. dsociety.cf) : ")
    subprocess.call(["nslookup",url])

else:
    stop
