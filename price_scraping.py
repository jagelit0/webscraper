# -*- coding: utf-8 -*-
#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
#import msvcrt

url = 'https://example.com' #URL
page = requests.get(url)
soup = BeautifulSoup(page.content ,"html.parser")
default = "109"

pre = soup.find('span', class_='overflow--wrap-off') #Scraping (CHANGE)
pre_text = pre.text
pre_act = pre_text.replace('€', '')

if default < pre_act :
    print("Ha bajado de precio -> " + '(' + str(pre_act) + '€' + ') [*]' )      #CHANGE
elif default > pre_act :
    print("Ha subido -> " + '(' + str(pre_act) + '€' + ') [*]' )
else :
   print("[*] Sigue igual -> " + '(' + str(pre_act) + '€' + ') [*]' )

#print("[!] Presiona una tecla para salir [!]")
#msvcrt.getch()
