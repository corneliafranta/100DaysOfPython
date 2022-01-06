from art import logo
import random

MAX_SCORE = 21

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def pick_cards(number_cards):
    """
    Randomly chooses a given amount of cards out of a provided list

    Parameters
    ----------
    number_cards: int

    Returns
    -------
    chosen_cards: list
        A list of randomly selected cards
    """
    chosen_cards = []

    for i in range(0, number_cards):
        chosen_cards.append(random.choice(cards))

    return chosen_cards

def calc_score(hand):
    """Returns the total of a given list of numbers"""
    score = sum(hand)

    return score
    # score = 0
    # for item in hand:
    #     score += item
    # return score

def display_current_score(score, hand):
    """Displays current score in the console"""
    print(f"Your cards: {hand}, current score: {score}")

def draw_next_card():
    """Asks player if they want to draw another card and runs through the process of choosing another card and
    adding it to the players hand"""
    draw_another_card = input("Type 'y' to draw another card, type 'n' to pass")

    if draw_another_card.lower() == 'y':
        players_cards.append(pick_cards(number_cards=1)[0])
        computers_cards.append(pick_cards(number_cards=1)[0])

        display_current_score(calc_score(players_cards), players_cards)
        return True

    return False

def evaluate_winner(players_score, computers_score):
    """Compares both scores and anounces the result"""
    print(f"Final Score: {players_score} : {computers_score}")

    if computers_score > 21 or players_score > computers_score  and not players_score > 21:
        print("Congratulations !!!! You won!!!")
    else:
        print("Oh nooo! You lost :(")


start_game = False
answer = input("Do you want to play a round of Black Jack? 'y' or 'n'")

if answer == "y":
    start_game = True


while start_game:
    print(logo)
    print("Welcome to this round of BlackJack")

    players_cards = pick_cards(number_cards=2)
    computers_cards = pick_cards(number_cards=2)

    display_current_score(calc_score(players_cards), players_cards)
    print(f"Computers first card: {computers_cards[0]}")

    while draw_next_card():
        if calc_score(players_cards) > MAX_SCORE or calc_score(computers_cards) > MAX_SCORE:
            break

    evaluate_winner(calc_score(players_cards), calc_score(computers_cards))
    restart_game = input("Do you want to play another round? 'y' or 'n' ")

    if restart_game.lower() == 'y':
        start_game = True
    else:
        break
