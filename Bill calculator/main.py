print("Bill calculator.")
bill = float(input("Enter your bill: "))
tip = int(input("How much tip you want to give? 10, 12 or 15?: "))
people = int(input("How many people to split the bill? "))

result = ((bill / 5) * (1 + tip / 100))
print("Each person should pay: $" "{:.2f}".format(result))
