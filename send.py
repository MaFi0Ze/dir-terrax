#!/usr/bin/env python
import threading
import string
import base64
import urllib.request
import urllib.parse
import os
import time
import sys
import random

try:
    import requests
except ImportError:
    print('Error !! : Some dependencies are not installed')
    print('Type \'bash requirements.sh\' to install all required packages')
    exit()

# colors
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
W = '\033[0m'
colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m']

# The Credit For This Code Goes To Panda Hackers https://github.com/HACK3RY2J/
# And The Contributors Mentioned At https://github.com/HACK3RY2J/ANon-SMS/
# If You Wanna Take Credits, Please Look Yourself Again!!

def clr():
	if os.name == 'nt':
		os.system('cls')

def Track() :
  TXTID = input("Enter Text ID of Anon-SMS \n\t -->>")
  os.system(f"curl https://textbelt.com/status/{TXTID}")
  input("\nPress Enter To Exit..")
  print("\nThanks For Using Anon-Sms..")
  print("\tWe Hope To See You Again\n Type bash Run.sh\n\tTo Run Again..")
  exit()

def update():
    stuff_to_update = ['send.py']
    for fl in stuff_to_update:
        dat = urllib.request.urlopen("https://raw.githubusercontent.com/in4osecurity/anonsms/master/" + fl).read()
        file = open(fl, 'wb')
        file.write(dat)
        file.close()
    print('\n\t\tUpdated Successfull !!!!')
    print('\tRun The Script Again...')
    exit()

clr()
try:
    urllib.request.urlopen('https://www.google.com')
except Exception:
    print("Error While Connecting To Internet!!!")
    print("\tPlease Connect To Internet To Continue...\n")
    input('Exiting....\n Press Enter To Exit....')
    exit()
for num in range(101):
    print('\rПроверка обновлений {}%'.format(num),end='',flush=True)
    time.sleep(random.uniform(0.0001,0.005))
    
#ver = urllib.request.urlopen("https://raw.githubusercontent.com/HACK3RY2J/Anon-SMS/master/.version").read().decode('utf-8')
verl = ''
try:
    verl = open(".version", 'r').read()
except Exception:
    pass
#if ver != verl:
#    print('\n\t\tAn Update is Available....')
#    print('\tUpdating Anon-SMS...')
#    update()
print("\rГотово                        ")
time.sleep(0.4)
print("Твоя версия самая свежая")
time.sleep(0.3)
print("\n===================\n")
print('\n\tStarting Anon-SMS...\n')
try:
#    noti = urllib.request.urlopen("https://raw.githubusercontent.com/HACK3RY2J/Anon-SMS/master/.notify").read().decode('utf-8')
    if len(noti) > 10:
        print('\nNotification : ' + noti + '\n')
except Exception:
    pass
    
    
time.sleep(0.5)
while True:
	print("\033[0mЭту утилиту можно использовать для отправки анонимных СМС-сообщений")
	break
type = 0
try:
	if sys.argv[1] == "track":
		type = 1
except Exception:
	type = 0
if type == 1:
	Track()
elif type == 0:
	while True:
		print("Введи данные о получателе и текст")
		cc = input("\tВведи код страны (без +) : ")
		if '+' in cc:
		        tc = list(cc)
		        tc.remove('+')
		        cc = ''.join(tc)
		        cc = cc.strip()
		if len(cc) >= 4 or len(cc) < 1:
		        print('\n\nInvalid Country Code..\n\t\tCountry Codes Are Generally 1-3 digits...\n')
		        continue
		pn = input("Введи номер телефона (после кода) : +" + cc + " ")
		if len(pn) <= 6:
		        print('\n\nНе правильный номер..\n')
		        continue
		numbe = cc + pn
		if not numbe.isdigit():
		            print('\n\nPhone Number Must Consist Of Numbers Only\n')
		            continue
		receiver = '+' + numbe
		text = input("Введи сообщение для отправки : ")
		
		resp = requests.post('https://textbelt.com/text',{
			'phone' : receiver,
			'message' : text ,
			'key' : 'textbelt'
		})
 
		print(resp.json())
		os.system('python back.py')
		exit() 
		break
		if '"success" : true ' in resp.text:
		    print("\033[92m Message Sent Succesfully \033[0m")
		if '"success" : false ' in resp.text:
		    print("\033[91m Error Occured")
		    print("\033[91m Failed to send SMS! ")
		os.system('python back.py')
		exit() 
