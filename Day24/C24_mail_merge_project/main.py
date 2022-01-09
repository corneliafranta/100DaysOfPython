# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open('./Input/Names/invited_names.txt') as name_file:
    names = name_file.read()
    names_list = names.split('\n')

with open('./Input/Letters/starting_letter.txt') as starting_letter_file:
    text = starting_letter_file.read()
    print(text)

for name in names_list:
    new_text  = text.replace('[name]', name)
    file_name = f'letter_for_{name}.txt'
    with open(f'./Output/ReadyToSend/{file_name}', 'w') as new_invitation:
        new_invitation.write(new_text)