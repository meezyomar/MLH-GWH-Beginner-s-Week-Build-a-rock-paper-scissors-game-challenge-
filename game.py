import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

def get_user_selection():
    choices = [f"{Action.name}[{Action.value}]" for Action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

def getWinner(userAction, computerAction):
    victories = {
        Action.Rock: Action.Scissors,
        Action.Paper: Action.Rock,
        Action.Scissors: Action.Paper
    }
    defeats = victories[userAction]
    if computerAction == userAction:
        return "Tie"
    elif computerAction == defeats:
        return "You Win!"
    else:
        return "You Lose!"
    
while True:
    try:
        userAction = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computerAction = get_computer_selection()
    print(getWinner(userAction, computerAction))
    
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
    