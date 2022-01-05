from data import MENU, resources, COINS, MASCHINE_NUMBER
from datetime import datetime

def take_order():
    order = input("What would you like? (espresso/latte/cappuccino")
    return order


def create_report():
    now = datetime.now()
    now_hrf = now.strftime("%d-%m-%Y-%H-%M-%S")
    file = open(f"Report-{now_hrf}", "w")
    file.write(f"Resources Report Machine N-{MASCHINE_NUMBER} Date: {now_hrf}")
    file.write("--------------------------------------------------------------------------------------------")
    for resource in resources:
        file.write(f"- {resource} :  {resources[resource]}")

    file.close()



# TODO 1 Take order from Customer
new_order = take_order()

# TODO 2 Turn the coffee machine off by entering 'off' to the prompt
machine_running = True
if new_order == "off":
    machine_running = False
elif new_order == "report":
    create_report()


# TODO 3 Print report


# TODO 4 Check resources sufficient

# TODO 5 Process coins

# TODO 6 Check if transaction was successful

# TODO 7 Make Coffee
