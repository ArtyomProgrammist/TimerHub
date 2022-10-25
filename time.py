from os import *
print("Installing pip...")
system("pip install pyfiglet")
system("clear")
from colorama import Fore as f
from pyfiglet import *
from time import *
result = figlet_format("Time", font = "doh")
print(f"{f.RED}{result}")
print(f"{f.GREEN}Выберите функцию:")
print("(1) 00:00:00")
print("(2) 00:00")
print("(3) Hour 00")
print("(4) Minute 00")
print("(5) Secound 00")
o = int(input("Напиши любую цифру, которую хотите функцию: "))
system("clear")
if o == 1:
    while True:
        sleep(1)
        local = localtime()
        timers = strftime("%H:%M:%S", local)
        print(f"{f.YELLOW}{timers}", end = "\r")
if o == 2:
        while True:
            sleep(1)
            local = localtime()
            timers = strftime("%H:%M", local)
            print(f"{f.YELLOW}{timers}", end = "\r")
if o == 3:
        while True:
            sleep(1)
            local = localtime()
            timers = strftime("%H", local)
            print(f"{f.YELLOW}{timers}", end = "\r")
if o == 4:
        while True:
            sleep(1)
            local = localtime()
            timers = strftime("%M", local)
            print(f"{f.YELLOW}{timers}", end = "\r")
if o == 5:
        while True:
            sleep(1)
            local = localtime()
            timers = strftime("%S", local)
            print(f"{f.YELLOW}{timers}", end = "\r")
