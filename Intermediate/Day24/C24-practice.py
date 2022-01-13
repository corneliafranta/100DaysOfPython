with open('text.txt') as file:
    contents = file.read()
    print(contents)


with open('text.txt', 'w') as file:
    file.write('New Text')