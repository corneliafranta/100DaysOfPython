import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

data_dic = {row.letter.lower(): row.code for (index, row) in data.iterrows()}


def spell_word():
    word = input('Enter a word: ')
    try:
        spelled_word = [data_dic[letter] for letter in word.lower()]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        spell_word()
    else:
        print(spelled_word)


spell_word()
