import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

data_dic = {row.letter.lower(): row.code for (index, row) in data.iterrows()}


def spell_word(word):
    spelled_word = [data_dic[letter] for letter in word.lower()]
    print(spelled_word)

word = input('Enter a word: ')
spell_word(word)
