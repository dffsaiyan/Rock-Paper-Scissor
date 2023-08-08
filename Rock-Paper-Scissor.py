from random import randint

print("Enter Rock, Paper, Scissor: ")
player = input()
computer = randint(0,2)

if computer == 0:
    computer = "Rock"
if computer == 1:
    computer = "Paper"
if computer == 2:
    computer = "Scissor"  

print("---")
print("You choose: " + player)
print("Computer chooses: " + computer)
print("---")

if player == computer:
    print("Draw")
else:   
    # Case 1: Scissor
    if player == "Scissor":
        if computer == "Rock":
            print("You Lose!")
        else:
            print("You Win!")
    # Case 2: Rock       
    elif player == "Rock":
        if computer == "Scissor":
            print("You Win!")
        else:
            print("You Lose!")
    # Case 3: Paper 
    elif player == "Paper":
        if computer == "Scissor":
            print("You Lose!")
        else:
            print("You Win!")
    else:
        print("Wrong input! Enter again.")

            