from contextlib import nullcontext
from os import startfile
from re import S
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep
import array as ar

def WhatsappMessage(name,message):
     
    startfile("C:\\Users\\Utkarsh Yadav\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    # test.py used
    sleep(6)
    #search button
    click(x=500, y=170)
    sleep(2)
    #writes name
    write(name)

    sleep(1)
    #selects the search result
    click(x = 500, y = 340)
    #sleep(0.1)
    #back button
    #click(x = 60, y = 170)

    sleep(1)
    write(message)

    sleep(0.2)
    click(x=1853, y=1028)
    sleep(0.1)
    click(x=1738, y=7)

#WhatsappMsg('keshav', 'hello1')


def WhatsappCall(name):
    startfile("C:\\Users\\Utkarsh Yadav\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    # test.py used
    sleep(1)
    click(x=500, y=170)

    sleep(0.5)
    write(name)

    sleep(1)
    click(x = 500, y = 340)
    click(x = 60, y = 170)
    click(x=1679, y=80)

    #to end the call
    sleep(3)
    click(x=1854, y=110)

    # to minimize whatsapp
    click(x=1765, y=9)

#WhatsappCall('mom')

def WhatsappVideo(name):
    startfile("C:\\Users\\Utkarsh Yadav\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    # test.py used
    sleep(1)
    click(x=500, y=170)

    sleep(0.5)
    write(name)

    sleep(1)
    click(x = 500, y = 340)
    click(x = 60, y = 170)
    click(x=1616, y=94)
    click(x=38, y=153)

    #to end the call
    sleep(3)
    click(x=1750, y=427)
    

    # to minimize whatsapp
    click(x=1765, y=9)

#WhatsappVideo('mom')

def WhatsappGroup(members):
    startfile("C:\\Users\\Utkarsh Yadav\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    # test.py used
    sleep(1)
    #group create
    click(x=627, y=83)
    sleep(0.1)
    #search
    click(x=540, y=164) 
    u = 70
    for i in members:
        write(i)
        sleep(0.5)
        #add member
        click(x=367, y=310 + u)
        #i = i+1

list = ['mom', 'lcg', 'sparsh', 'tejas']
#WhatsappGroup(list)


def WhatsappOpenChat(name):
    startfile("C:\\Users\\Utkarsh Yadav\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    # test.py used
    sleep(1)
    click(x=500, y=170)

    write(name)

    sleep(1)
    click(x = 500, y = 340)
    click(x = 60, y = 170)
#WhatsappOpenChat('mom')