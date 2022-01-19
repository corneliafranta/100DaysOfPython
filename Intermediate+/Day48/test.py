string = 'ahfaerur24qHUHEUHEU'

def find_first_single_occuring_character(text):
    for letter in text.lower():
        if letter != ' ':
            occurence = text.count(letter.lower())
            if occurence == 1:
                return letter

    return None


print(find_first_single_occuring_character(string))