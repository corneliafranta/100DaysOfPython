# try/catch

try:
    file = open('a_file.txt')
    a_dictionary = {'key': 'value'}
    print(a_dictionary['dajhfdjhfa'])
except FileNotFoundError:
    file = open('a_file.txt', 'w')
except KeyError as error_message:
    print(f"That key {error_message} does not exist")
else:
    content = file.read()
    print(content)

height = float(input("Height: "))
weight = float(input("Weight: "))

# raise Exception

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")
bmi = weight / height ** 2
print(bmi)
