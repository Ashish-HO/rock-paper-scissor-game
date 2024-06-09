import random

COMPUTER_POINTS = 0
USER_POINTS = 0
ROUND = 5


def valid_input():
    while True:
        a = input(
            "Enter 'r' for rock , 'p' for paper or 's' for scissor or  q to quit."
        ).lower()

        if a == "r" or a == "p" or a == "s":
            return a
            break
        elif a == "q":
            print("Good Bye !!")
            exit(0)
        else:
            print("Invalid input")


options = ["r", "p", "s"]

computer_pick = random.choice(options)

print(f"computer picks {computer_pick}.")


while ROUND:
    user_pick = valid_input()

    if computer_pick == "r" and user_pick == "p":
        print("You win .")
        USER_POINTS += 1
        ROUND -= 1

    if computer_pick == "P" and user_pick == "s":
        print("You win .")
        USER_POINTS += 1
        ROUND -= 1

    if computer_pick == "s" and user_pick == "r":
        print("You win .")
        USER_POINTS += 1
        ROUND -= 1

    elif computer_pick == user_pick:
        print("Draw")
        ROUND -= 1
    else:
        print("You lose.")
        COMPUTER_POINTS += 1
        ROUND -= 1

if COMPUTER_POINTS < USER_POINTS:
    print(f"YOU WON !! :) by {USER_POINTS-COMPUTER_POINTS} points.")
elif COMPUTER_POINTS == USER_POINTS:
    print("Draw")
else:
    print(f"YOU LOOSE :( by {COMPUTER_POINTS-USER_POINTS} points.")
