import random

print("Random choice of input")
names = str(input("Enter names: "))
names_split = names.split(", ")
pay_int = random.randint(0, len(names_split))
pay = names_split[pay_int - 1]

print(pay)