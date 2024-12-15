import os
import time
from startup_vars import *

os.system('cls')
ask = input("Have an account [?] ")

if ask == "n" or ask == "no" or ask == "No" or ask == "N":
    user = input("User [?] ")
    ask = input("Set a password [?] ")
    if ask == "n" or ask == "no" or ask == "No" or ask == "N":
        passw = "n53hj7"
    else:
        passw = input("Password [?] ")
    f = open('user.ut','w')
    f.write(user)
    f.close()
    f = open('pw.ps','w')
    f.write(passw)
    f.close
    print("Rebooting........")
    time.sleep(3)
    os.startfile("os.py")

else:
   print("Please wait.")
   time.sleep(2)
   os.startfile("os.py")