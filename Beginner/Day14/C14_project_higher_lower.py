import random
import art
from game_data import data

data = data


def select_accounts(amount):
    selected_data = random.choices(data, k=amount)
    if selected_data[0] == selected_data[1]:
        select_accounts(amount)
    return selected_data


def format_data(account):
    return f"{account['name']}, {account['description']} from {account['country']}"


def evaluate_choice(choice, game_data, return_right_answer):
    right_answer = {}
    is_correct = False
    if choice == 'a':
        if game_data[0]['follower_count'] > game_data[1]['follower_count']:
            right_answer = game_data[0]
            is_correct = True
    else:
        if game_data[1]['follower_count'] > game_data[0]['follower_count']:
            right_answer = game_data[1]
            is_correct = True

    if not is_correct:
        if choice == 'a':
            right_answer = game_data[0]
        else:
            right_answer = game_data[1]

    if return_right_answer:
        return right_answer
    else:
        return is_correct


def run_game():
    score = 0

    accounts = select_accounts(2)
    keep_playing = True

    while keep_playing:
        print(art.logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
        print(f"Compare A: {format_data(accounts[0])}")
        print(art.vs)
        print(f"Against: {format_data(accounts[1])}")
        choice = input("Who has more followers= Type 'A' or 'B' ").lower()
        answer_right = evaluate_choice(choice, accounts, return_right_answer=False)
        right_answer = evaluate_choice(choice, accounts, return_right_answer=True)
        if answer_right:
            score += 1
            accounts = [right_answer, select_accounts(1)[0]]
        else:
            keep_playing = False

    print(f"Sorry, that's wrong. Final score: {score}")


run_game()
