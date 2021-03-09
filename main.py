import random

user_selects = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_selects = random.choice(possible_actions)
print("You chose ", user_selects, ", computer chose ", computer_selects, ".")

if user_selects == computer_selects:
    print(f"Both players selected ", user_selects, ". It's a tie!")
elif user_selects == "rock":
    if computer_selects == "scissors":
        print("Rock smashes scissors! You won!")
    else:
        print("Paper covers rock! You lost.")
elif user_selects == "paper":
    if computer_selects == "rock":
        print("Paper covers rock! You won!")
    else:
        print("Scissors cuts paper! You lost.")

elif user_selects == "scissors":
    if computer_selects == "paper":
        print("Scissors cuts paper! You won!")
    else:
        print("Rock smashes scissors! You lost.")
