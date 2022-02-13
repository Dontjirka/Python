print("Love calculator")
name1 = str(input("Your name: ").lower())
name2 = str(input("Their name: ").lower())

love1 = "true"
love2 = "love"

result = name1.count("t")
result += name1.count("r")
result += name1.count("u")
result += name1.count("e")
result += name2.count("t")
result += name2.count("r")
result += name2.count("u")
result += name2.count("e")

result1 = name1.count("l")
result1 += name1.count("o")
result1 += name1.count("v")
result1 += name1.count("e")
result1 += name2.count("l")
result1 += name2.count("o")
result1 += name2.count("v")
result1 += name2.count("e")

r = str(result)
r1 = str(result1)

is_love = int((r + r1))

if is_love < 10 or is_love > 90:
    print(f"Your score is {is_love} you're such a good couple.")
if is_love >= 40 and is_love <= 50:
    print(f"Your score is {is_love} you're alright together.")
else:
    print(f"Your score is {is_love}.")