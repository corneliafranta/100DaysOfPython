from data import MENU, resources, MASCHINE_NUMBER
from datetime import datetime
from art import logo

current_resources = resources


def take_order():
    order = input("What would you like? (espresso/latte/cappuccino) ")
    return order


def create_report():
    now = datetime.now()
    now_file_name = now.strftime("%d-%m-%Y-%H-%M-%S")
    now_hrf = now.strftime("%d.%m.%Y %H:%M:%S")
    file = open(f"Report-{now_file_name}", "w")
    file.write(f"Resources Report Machine N-{MASCHINE_NUMBER} Date: {now_hrf} \n")
    file.write("-------------------------------------------------------------------------------------------- \n \n")
    for resource in current_resources:
        file.write(f"- {resource} :  {current_resources[resource]} \n")

    file.close()


def check_resource_sufficiency(drink):
    required_ingredients = drink['ingredients']
    missing_ingredients = []
    for ingredient in required_ingredients:
        if required_ingredients[ingredient] > current_resources[ingredient]:
            missing_ingredients.append(ingredient)

    if len(missing_ingredients) > 0:
        return missing_ingredients

    return None


def add_quaters(amount):
    return 0.25 * amount


def add_dimes(amount):
    return 0.10 * amount


def add_nickles(amount):
    return 0.05 * amount


def add_pennies(amount):
    return 0.01 * amount


def process_coins():
    number_quaters = int(input("How many quarters? "))
    number_dimes = int(input("How many dimes? "))
    number_nickles = int(input("How many nickles? "))
    number_pennies = int(input("How many pennies? "))
    sum_coins = add_quaters(number_quaters)
    sum_coins += add_dimes(number_dimes)
    sum_coins += add_nickles(number_nickles)
    sum_coins += add_pennies(number_pennies)
    return sum_coins


def validate_payment(given_amount, required_amount):
    if given_amount >= required_amount:
        return given_amount - required_amount


def prepare_beverage(beverage, beverage_name):
    ingredients = beverage['ingredients']
    for ingredient in ingredients:
        current_resources[ingredient] -= ingredients[ingredient]
    print(f"Here is your {beverage_name} ☕, Enjoy!")


def handle_payment(required_amount):
    given_amount = process_coins()
    successful_payment = validate_payment(given_amount, required_amount)
    if successful_payment is not None:
        print(f"The transaction was successfull. Your change: ${successful_payment}")
        current_resources['money'] += required_amount
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


machine_running = True
print(logo)
while machine_running:
    new_order = take_order()
    if new_order == "off":
        machine_running = False
    elif new_order == "report":
        create_report()
    else:
        ordered_item = MENU[new_order]
        resources_missing = check_resource_sufficiency(ordered_item)
        if not resources_missing:
            print(f"This item costs ${ordered_item['cost']}")
            print(float(ordered_item['cost']))
            payment_successful = handle_payment(float(ordered_item['cost']))
            if payment_successful:
                prepare_beverage(ordered_item, new_order)
        else:
            print(f"Please make another order we have run out of {' and '.join(resources_missing)}")
