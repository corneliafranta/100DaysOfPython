import random
import C7_hangman_art
import C7_hangman_words

stages = C7_hangman_art.stages
word_list = C7_hangman_words.word_list
logo = C7_hangman_art.logo

picked_word = random.choice(word_list)
all_letters_guessed = False
game_won = False
lives = 6
guessed_letters = []
print(logo)
print("PSST the choosen word is " + picked_word)

display = []

for char in picked_word:
    display += "_"


def validate_guess(users_guess, word, lives_left):
    for index, letter in enumerate(word):
        if letter == users_guess.lower():
            display[index] = letter
    guessed_letters.append(letter)


while not all_letters_guessed and lives > 0:
    guess = input("Guess a letter. ")
    if guess in guessed_letters:
        print(f"You already guessed {guess}")
    else:
        validate_guess(guess, picked_word, lives)
        if guess not in picked_word:
            lives -= 1
            print(
                f"You guessed {guess}, that's not in the word. You lose a life."
            )

        if "_" not in display:
            all_letters_guessed = True
            game_won = True
        guessed_letters.append(guess)

    print(stages[lives])
    print(f"{' '.join(display)}")
if game_won:
    print("Congrats, you won")
else:
    print("You lost")
