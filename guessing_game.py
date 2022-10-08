from random import randint
random_number = randint(1,10)
while True:
    guess = input("Pick a number from 1 - 10 : ")
    guess = int(guess)
    if guess < random_number:
        print("TOO LOW!")
    elif guess > random_number:
        print("TOO HIGH!")
    else:
        print("YOU WON!")
        play_again = input("Do you want to play again? (Y/N) ")
        if play_again == "Y":
            random_number = randint(1,10)

            continue;
        else:
            print("Thank you for playing!")
        break