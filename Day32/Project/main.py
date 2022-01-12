import datetime as dt
import random
import smtplib

import pandas


def get_birthday_data():
    try:
        birthday_data = pandas.read_csv('birthdays.csv').to_dict(orient='records')

    except FileNotFoundError:
        print('No such File')
    else:
        return birthday_data


# 2. Check if today matches a birthday in the birthdays.csv
def has_birthday(day, month):
    now = dt.datetime.now()
    return is_same_day(day, now.day) and is_same_month(month, now.month)


def is_same_day(day1, day2):
    return day1 == day2


def is_same_month(month1, month2):
    return month1 == month2


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
def send_birthday_wishes(pers):
    text = get_text()
    text = text.replace('[NAME]', pers['name'])
    my_email = 'corneliaDeGossonDeVarennes@gmail.com'
    password = '1234Test'
    subject = "Happy Birthday"
    message = f"Subject:{subject}\n\n{text}"
    print(pers['email'])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=pers['email'], msg=message)


def get_text():
    card_text = ""
    file_names = ['letter_1', 'letter_2', 'letter_3']
    try:
        with open(f'letter_templates/{random.choice(file_names)}.txt') as text_file:
            card_text = text_file.read()

    except FileNotFoundError:
        print("File couldn't be found")
        card_text = "Dear [NAME] \n I wish you all the best for your birthday \n Best Regards \n Cornelia"

    return card_text


birthday_data = get_birthday_data()

for person in birthday_data:
    print(person)
    if has_birthday(person['day'], person['month']):
        send_birthday_wishes(person)

# 4. Send the letter generated in step 3 to that person's email address.
