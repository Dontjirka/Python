print("BMI calculator")
weight = int(input("Enter your weight in kg: "))
heigt = float(input("Enter your height in cm: "))

result = weight / heigt**2

if result < 18.5:
    print("You're underweight.") 
elif result < 25:
    print("You have normal weight.")
elif result < 30:
    print("You're slightly overweight.")
elif result < 35:
    print("You're obese.")
else:
    print("You're almost dead, get some help.")