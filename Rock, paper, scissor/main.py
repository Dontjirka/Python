import random as rand

print("Rock, paper, scissor game.")
player = str(input("Enter R for (Rock), P for (Paper) or S for (scissor): "))
game = ["Rock", "Paper", "Scissor"]
computer = str(rand.choices(game))

#Rock
if computer == "['Rock']":
    if player == "R":
        print("Tie")
    elif player == "S":
        print("You lose")
    else:
        print("You win")
#Paper
if computer == "['Paper']":
    if player == "P":
        print("Tie")
    elif player == "R":
        print("You lose")
    else:
        print("You win")
#Scissor
if computer == "['Scissor']":
    if player == "S":
        print("Tie")
    elif player == "P":
        print("You lose")
    else:
        print("You win")