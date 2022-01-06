from art import logo

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def devide(num1, num2):
    return num1 / num2


operations = {
    '+' : add,
    '-' : subtract,
    '*': multiply,
    '/': devide
}

def run_calculator(num_one= None):
    if not num_one:
        num_one = float(input("Enter your first number. "))
    for operation in operations:
        print(operation)
    operator = input("Pick an operation from the line above. ")
    num_two = float(input('Enter your second number'))
    calc_function = operations[operator]
    result = calc_function(num_one, num_two)
    print(f"{num_one} {operator} {num_two} = {round(result, 2)}")
    return result

should_continue = True
previous_result = None
while should_continue:
    if not previous_result:
        print(logo)
        previous_result = run_calculator()
    else:
        previous_result = run_calculator(previous_result)

    answer_should_exit = input("Do you want to continue to calculate with your result (yes), start a new calculation (new) or do you want to exit (no)")

    if answer_should_exit.lower() == "no":
        should_continue = False
    elif answer_should_exit.lower() == "new":
        previous_result = None

print("Thank you for using this calculator :) ")





