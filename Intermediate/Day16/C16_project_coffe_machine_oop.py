from moneyMachine import MoneyMachine
from menu import Menu, MenuItem
from coffeeMaker import CoffeeMaker


def take_order():
    order = input("What would you like? (espresso/latte/cappuccino) ")
    return order

machine_running = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while machine_running:
    new_order = take_order()
    if new_order == "off":
        machine_running = False
    elif new_order == "report":
        coffee_maker.report()
    else:
        ordered_item = menu.find_drink(new_order)
        resources_available = coffee_maker.is_resource_sufficient(ordered_item)
        if resources_available:
            cost= ordered_item.cost
            print(f"This item costs ${cost}")
            payment_successful = money_machine.make_payment(cost)
            if payment_successful:
                coffee_maker.make_coffee(ordered_item)
        else:
            print("Please make another order we dont have all the ingredients...")
