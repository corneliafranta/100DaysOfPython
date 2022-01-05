import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_attempts():
    """
        Asks User for preferred level of difficulty and returns corresponding number of attempts

        RETURN
        ---------

        attempts: Integer

        Returns number of attempts corresponding to chosen level of difficulty in form of an integer

    """
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Invalid choice")
        set_attempts()


def make_guess(attempts):
    """
    Lets User enter an integer
    :return:
     guess: Integer
    """
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    return guess


def select_number():
    """
    Selects Random number between 1 and 100
    """
    return random.randint(1, 101)


def evaluate_guess(guess, game_number):
    """
    Compares both entered numbers. And evaluates there relation
    :param guess: number guessed by the user
    :param game_number: number randomly created
    :return: returns either 'match' if both numbers are identical or 'high'/'low' depending
    if guess is higher or lower then game_number
    """
    if guess == game_number:
        return "match"
    elif guess > game_number:
        return "high"
    else:
        return "low"


def game_play():
    """
    Executes the number guessing game and loops through until the game is either lost or won
    """
    print(logo)
    print("""Welcome to the Number Guessing Game!
    I am thinking of a number between 1 and 100.
    """)
    attempts = set_attempts()
    NUMBER = select_number()

    run_game = True
    while run_game:
        guess = make_guess(attempts)
        result = evaluate_guess(guess=guess, game_number=NUMBER)

        if result == "match":
            print(f"You got it! The answer was {NUMBER}")
            run_game = False
            game_won = True
        else:
            print(f"Too {result}")
            print("Guess again.")
            attempts -= 1

        if attempts == 0:
            run_game = False
            print("You've run out of guesses, you lose.")


game_play()
