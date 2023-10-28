import random

userInput = input("Pick a option: rock, paper or scissors(case-sensitive)\n")
if userInput == "rock":
    userInput = 1
elif userInput == "paper":
    userInput = 2
elif userInput == "scissors":
    userInput = 3
else:
    print("Invalid choice. Check your spelling. Remember, options are case sensitive.")
    exit()

compInput = random.randint(1, 3)
if compInput == 1:
    print("Computer chose rock so..")
elif compInput == 2:
    print("Computer chose paper so...")
else:
    print("Computer chose scissors so...")

#Tie   
if userInput == compInput:
    print("You tied with the bot.")

#Chooses rock
elif userInput == 1 and compInput == 2:
    print("You lose!😢")
elif userInput == 1 and compInput == 3:
    print("You win!😁")
# Chooses paper
elif userInput == 2 and compInput == 1:
    print("You win!😁")
elif userInput == 2 and compInput == 3:
    print("You lose!😢")
#Chooses scissors
elif userInput == 3 and compInput == 1:
    print("You lose!😢")
elif userInput == 3 and compInput == 2:
    print("You win!😁")
