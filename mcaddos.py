import os,sys

try:
    import sys, socks, requests, wget, cfscrape, urllib3
except:
    if sys.platform.startswith("linux"):
        os.system("pip install pysocks requests wget cfscrape urllib3 scapy")
    elif sys.platform.startswith("freebsd"):
        os.system("pip install pysocks requests wget cfscrape urllib3 scapy")   
    else:
        os.system("pip install pysocks requests wget cfscrape urllib3 scapy")

import socket, socks, threading, random, re, os
import sys, glob, time, requests, ssl, webbrowser
import bz2, datetime, wget, json, cfscrape, urllib3
from time import sleep
from os import system
from sys import stdout
from scapy.all import *
from random import randint
import time

R = '\033[1;91m'
V = '\033[1;95m'
W = '\033[1;97m'
G = '\033[1;92m'
N = '\033[1;0m'
Y = '\033[1;93m'
 
for i in range(1):
	os.system("clear")
 
urllib3.disable_warnings()
urllib3.PoolManager()
 
useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",]    
#WagMoNgPalitanHAHA
black_lists = ["arrahmah.id"]
black_lists = ["republika.co.id"]
 
 
def logo():
    if sys.platform.startswith("linux"):
        os.system('clear')
    elif sys.platform.startswith("freebsd"):
        os.system('clear')
    else:
        os.system('color ' +random.choice(['a', 'b', 'c', 'd'])+ " & cls & title [+] ANONPRIXOR LDAP FLOOD [+]")     
        os.system("figlet -f  slant  mca2022")
     print(G+'''

\t $$$$$$$\  $$$$$$$\              
\t $$  __$$\ $$  __$$\               
\t $$ |  $$ |$$ |  $$ | $$$$$$\   $$$$$$$\ 
\t $$ |  $$ |$$ |  $$ |$$  __$$\ $$  _____|
\t $$ |  $$ |$$ |  $$ |$$ /  $$ |\$$$$$$\  
\t $$ |  $$ |$$ |  $$ |$$ |  $$ | \____$$\ 
\t $$$$$$$  |$$$$$$$  |\$$$$$$  |$$$$$$$  |
\t \_______/ \_______/  \______/ \_______/

\t ************ Moslem Cyber Army **********
\t ~~~~~~~~~~~~~ A    S    C   A ~~~~~~~~~~~

\t =========[%s MCA DDos V1.0 %s]===========  
\t          Version : python 1.x.x.           
\t              UNLIMITED TIME!               
\t   ReproClone By JazCyberTeam|21/02/2022    
\t =========================================  
''')

    try:
        print("\n[*] Target : "+W+str(url_main)+ ":" +str(port)+G)
    except:
        pass
    try:
        print(G+"[*] Method  "+W+str(name_method_attack)+G)
    except:
        pass
    try:
        print(G+"[*] Mode   : "+W+str(filenam2)+G)
    except:
        pass      
    try:
        print(G+"[*] Threads: "+W+str(threads)+G)
    except:
        pass
 
 
 
def start_url():
    global url, url_main, host_url, host_ip, port
    if sys.platform.startswith("linux"):
        pass
    elif sys.platform.startswith("freebsd"):
        pass
    else:
        path = "C:/Program Files/nodejs/node.exe"
        if (not os.path.isfile(path)):
            print("[!] Please Install NodeJs. Downloading... [!]")
            down = wget.download("https://nodejs.org/dist/v12.13.0/node-v12.13.0-x64.msi")
            down
            os.system("node-v12.13.0-x64.msi")
    logo()
    url = input("\n[*] Target [URL/IP]: ").strip()
    if url == "":
        start_url()
    url_main = url
    try:
        host_url = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
    except:
        host_url = url.replace("http://", "").replace("https://", "").split("/")[0]
    if host_url in black_lists:
       print("\n[X] ERROR: Site In Backlits")
       sleep(4)
       url      = ""
       url_main = ""
       start_url()
    host_ip = socket.gethostbyname(host_url)
    start_port()
    logo()
    choice_method_attack()
 
def start_port():
    global port
    print("[+]-----------------------------[+]")
    port = str(input("[*] Port [80]: "))
    if port == '':
        if "https" in url:
                port = int(443)
                print("[!] Selected Port = 443 [!]")
        else:
            port = int(80)
            print("[!] Selected Port = 80 [!]")
    else:
        port = int(port)
def start_mode():
    global choice_mode, filenam1, filenam2, method_pass_cf
    print("""
[+]=======[ LAYER 4 ]======[+]
[+]1. LDAP  [ HOME CONNECTION]                       
[+]========================[+]
""")
 
    choice_mode = input("[*] Attack Mode [1]: ")
    if choice_mode == "1":
        filenam2 = "LDAP"
        logo()
        numthreads()
    else:
        print (R+"[!] You Mistyped, try again [!]\n"+N)
        start_mode()
error_cf = int(0)
def choice_method_attack():
    global method_attack, name_method_attack
    print("[+]-----------------------------[+]")
    print("[+] 1: Request [ Normal ]")
    method_attack = input("[*] Choice Request [1]: ")
    if (method_attack == "1") or (method_attack == ""):
        name_method_attack = "Normal"
        print("[!] Selected Method Attack Normal")
        method_attack = "1"
    else:
        print ("[!] You mistyped, try again [!]\n")
        choice_method_attack()
    logo()
    start_mode()
 
def numthreads():
	try:
		threads = int(input("[*] Threads [2000]: "))
		for i in range(1):
			print("[!] Selected Threads "+str(threads)+" [!]\n Please Wait~!")
			time.sleep(10)
			for i in range(9999999999999999999):
				print("\033[01;31m[+] LDAPddos Virus Terkirim")
				time.sleep(0.0)
	except ValueError:
		print(W+"["+G+"!"+W+"]"+R+" Missed Threads"+G)
		numthreads()
 
 
if __name__ == '__main__':
   start_url();
