import random

# Declaring Variables
"""
player_choice = "rock"
computer_choice = "paper"
"""


# Creating functions
def get_choices():
    player_choice = input("Enter your choice(rock, paper, scissor): ")
    comp_choices = ["rock", "paper", "scissors"]  # List in Python
    computer_choice = random.choice(comp_choices)

    # using dictionaries in Python
    choices = {"Player": player_choice, "Computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"Your choice = {player}\nComputer's choice = {computer}")
    if player == computer:
        return "It's a TIE"

    elif player == "rock":
        if computer == "paper":
            return "Paper covers rock, YOU LOSE:/"
        else:
            return "Rock smashes Scissor, YOU WIN!!"

    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock, YOU WIN!!"
        else:
            return "Scissor cuts the paper, YOU LOSE:/"

    else:
        if computer == "rock":
            return "Rock smashes scissor, YOU LOSE:/"
        else:
            return "Scissor cuts the paper, YOU WIN!!"

choice = get_choices()

result = check_win(choice["Player"], choice["Computer"])
print(result)


name = input("Enter your name: ")
print("Hello "+name)
