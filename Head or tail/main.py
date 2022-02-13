import random as rand

coin = ["Head", "Tail"]
flip = str(rand.choices(coin))
if flip == "['Head']":
    print("It's a head")
if flip == "['Tail']":
    print("It's a tail")