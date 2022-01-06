print("Welcome to the tip calculator.")
total =float(input("What was the total bill? "))
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip_percentage = float(f"1.{tip_percentage}")
print(tip_percentage)
amount_people = int(input("How many people are sharing the bill? "))

amount_to_pay_per_person = total / amount_people  * tip_percentage

print(f"Each person should pay: ${round(amount_to_pay_per_person, 2)}")