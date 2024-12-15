import math
import time

print("Loading Calculater...")
time.sleep(1.3)
print("Done!!")
print("Always Rounds Down :(")
while True:
    num1 = input("First number ")
    operatator = input("Operation ")
    num2 = input("Second Number ")
    
    if num1 == "quit" or num2 == "quit" or operatator == "quit":
        quit()
    if operatator == "+":
        resault = float(num1) + float(num2)
    if operatator == "-":
        resault = float(num1) - float(num2)
    if operatator == "x" or operatator == "*":
        resault = float(num1) * float(num2)
    
    print(int(resault))