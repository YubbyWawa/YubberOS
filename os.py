import os
import time
import pygame
from startup_vars import *

pygame.init()

os.system('cls')

def onLoginRepeat():
    Select = input()
    if Select == "#":
        os.startfile('Apps\\calc.py')
    if Select == "<<.":
        os.startfile("Apps\\Magwah.py")
def onLogin():
    print(Apps)

user_name = open('user.ut')
passw = open('pw.ps')
u_n = user_name.read()
u_p = passw.read()

tries = 0
Loggedin = False

print("Welcome", u_n)
if u_p == "n53hj7":
    Loggedin = True
else:
    print("Please enter your password")

while tries <= 3 and Loggedin == False:
    if input() == u_p:
        print("Enjoy Yubber")
        time.sleep(1)
        os.system('cls')
        Loggedin = True
    else:
        print("Wrong password")
        tries = tries + 1
time.sleep(1)
if Loggedin:
    onLogin()
    while True:
        onLoginRepeat()