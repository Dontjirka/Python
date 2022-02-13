print("Leap year")
"""
###########################################################
For more info about leap year, visit this video (not mine): 
https://www.youtube.com/watch?v=xX96xng7sAE
###########################################################
"""
year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print ("Leap year.")
        else:
            print ("Not leap year.")
    else:
        print("Leap year.")
else:
    print ("Not leap year.")