import random as rand

print("Rock, paper, scissor game.")
player = str(input("Enter R for (Rock), P for (Paper) or S for (scissor): "))
game = ["Rock", "Paper", "Scissor"]
computer = str(rand.choices(game))

#Rock
if computer == "['Rock']":
    if player == "R":
        print("Robot: Rock")
        print("You: Rock")
        print("It's tie")
    elif player == "S":
        print("Robot: Rock")
        print("You: Scissor")
        print("You lose")
    else:
        print("Robot: Rock")
        print("You: Paper")
        print("You win")
#Paper
if computer == "['Paper']":
    if player == "P":
        print("Robot: Paper")
        print("You: Paper")
        print("It's tie")
    elif player == "R":
        print("Robot: Paper")
        print("You: Rock")
        print("You lose")
    else:
        print("Robot: Paper")
        print("You: Scissor")
        print("You win")
#Scissor
if computer == "['Scissor']":
    if player == "S":
        print("Robot: Scissor")
        print("You: Scissor")
        print("It's tie")
    elif player == "P":
        print("Robot: Scissor")
        print("You: Paper")
        print("You lose")
    else:
        print("Robot: Scissor")
        print("You: Rock")
        print("You win")
