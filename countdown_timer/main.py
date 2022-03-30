import time
from os import system, name

def clear():
   # for windows
   if name == 'nt':
        _ = system('cls')

   # for mac and linux
   else:
        _ = system('clear')

def countdown():
    Time = int(input("Enter seconds: "))
    timing = True
    while timing is not False:
        for i in range(Time+1):
            print(f"Remaining time is {Time}s")
            Time -= 1
            time.sleep(1)
            clear()
            if Time == 0:
                timing = False
    print("Ran out of time")

clear()
countdown()
