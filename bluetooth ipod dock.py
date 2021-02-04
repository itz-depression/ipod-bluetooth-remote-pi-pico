#impoting crap
from machine import UART, Pin
import time

#start serial on with the hc-05
blue = UART (0,9600)

#the buttons
play = Pin(26, Pin.OUT)
volup = Pin(20, Pin.OUT)
voldown = Pin(22, Pin.OUT)
next = Pin(27, Pin.OUT)
last = Pin(18, Pin.OUT)
menu = Pin(21, Pin.OUT)

#the yandere simulator code 
while True:
    msg = blue.read(1)
    print(msg)
#play and pause
    if "0" in msg:
        play.value(1)
        print("IPOD: PLAY/PAUSE")
        time.sleep(0.05)
        play.value(0)      
    elif "1" in msg:
#volume up this time hopefuly not the fucking run pin like wtf was you thinking AHHHH
        volup.value(1)
        time.sleep(0.05)
        print("IPOD: VOL+")
        volup.value(0)
    elif "2" in msg:
#volume down
        voldown.value(1)
        time.sleep(0.05)
        print("IPOD: VOL-")
        voldown.value(0)
    elif "3" in msg:
#next
        next.value(1)
        time.sleep(0.05)
        print("IPOD: NEXT")
        next.value(0)
    elif "4" in msg:
#last this time not useing the fucking gnd pin
        last.value(1)
        time.sleep(0.05)
        print("IPOD: LAST")
        last.value(0)
    elif "5" in msg:
#menu
        menu.value(1)
        time.sleep(0.05)
        print("IPOD: MENU")
        menu.value(0)