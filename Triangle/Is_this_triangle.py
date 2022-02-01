a = float(input("Enter one side of triangle (a): "))
b = float(input("Enter second side of triangle (b): "))
c = float(input("Enter third side of triangle (c): "))

if a + b > c and a + c > b and b + c > a:
    print("It is a triangle")
else:
    print("It is not a triangle")
