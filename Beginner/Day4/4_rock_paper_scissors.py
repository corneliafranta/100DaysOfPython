import random

possible_choices = ["rock", "paper", "scissors"]

players_choice= possible_choices[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))]
computers_choice = random.choice(possible_choices)
def printImage(choice):
    if choice == "rock":
        return '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
    elif choice == "paper":
        return '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
    else: return '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print(printImage(players_choice))
print("Computer chose: ")
print(printImage(computers_choice))

def evaluateGame(choice_one, choice_two):
    has_won = False
    is_draw = False
    if choice_one == possible_choices[0]:
        if choice_two == possible_choices[2]:
            has_won = True
        elif choice_two == possible_choices[0]:
            is_draw = True
    elif choice_one == possible_choices[1]:
        if choice_two == possible_choices[0]:
            has_won = True
        elif choice_two == possible_choices[1]:
            is_draw = True
    elif choice_one == possible_choices[2]:
        if choice_two == possible_choices[0]:
            has_won = True
        elif choice_two == possible_choices[2]:
            is_draw = True

    return {"has_won": has_won, "is_draw": is_draw}

result = evaluateGame(players_choice, computers_choice)

if result["has_won"]:
    print("You won !!!")
elif result["is_draw"]:
    print("Its a draw .....")
else:
    print("You lost :(")
