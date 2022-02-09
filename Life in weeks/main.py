print("Life in weeks")
age = int(input("Enter your age: "))

x = (90 * 365) - (age * 365)
y = (90 * 52) - (age * 52)
z = (90 * 12) - (age * 12)

print(f"You have {x} days, {y} weeks, and {z} months left.")
