from random import randint

player = input("Player, make your move: ").lower()
rand_number = randint(0,2)
if rand_number == 0:
    computer = "rock"
elif rand_number == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"computer plays: {computer}")
if player == computer:
    print("It's a tie!!!")
elif player == "rock":
    if computer == "scissors":
        print("player wins!")
    else:
        print("computer wins!")
elif player == "scissors":
    if computer == "rock":
        print("computer wins!")
    else:
        print("player wins!")
elif player == "paper":
    if computer == "rock":
        print("player wins!")
    else:
        print("computer wins!")
else:
    print("Make a valid move please!!!")