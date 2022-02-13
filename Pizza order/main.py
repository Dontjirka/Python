import sys

print("Welcome to pizza delivery!")
pizza_size = input("What size of pizza do you want? (S, M, L): ")
bill = 0

if pizza_size == "S":
    bill += 15
elif pizza_size == "M":
    bill += 20
elif pizza_size == "L":
    bill += 25
else:
    sys.exit("You might choosen some 'size' we don't provide... yet")

cheese = input("Do you want extra cheese? (Y/N): ")
if cheese == "Y":
    bill += 1

pepperoni = input("Do you want extra pepperoni? (Y/N): ")
if pepperoni == "Y":
    if pizza_size == "S":
        bill += 2
    else:
        bill += 3
print(f"Your finall bill is ${bill}")
