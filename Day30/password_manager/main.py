import json
from random import randint, shuffle, choice
from tkinter import *
from tkinter import messagebox
import pyperclip

LABELS = [{'text': 'Website: ', 'position': [1, 0]}, {'text': 'Email/Username: ', 'position': [2, 0]},
          {'text': 'Password: ', 'position': [3, 0]}]

STANDARD_EMAIL = 'franta-cornelia@gmx.at'


# ----------------------------- SEARCH FUNCTION ---------------------------------- #

def search():
    website = website_input.get()
    try:
        with open('my_pws.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Not Found", message="No data saved")
    else:
        if website in data:
            account_data = data[website]
            messagebox.showinfo(title=website,
                                message=f"Email: {account_data['email']}\nPassword: {account_data['password']}")
        else:
            messagebox.showerror(title="Not Found", message="No data saved for this website")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    created_pw = []
    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]

    created_pw.extend(password_letters)
    created_pw.extend(password_numbers)
    created_pw.extend(password_symbols)

    shuffle(created_pw)

    created_pw = ''.join(created_pw)
    password_input.insert(0, created_pw)
    pyperclip.copy(created_pw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {
        "email": email,
        'password': password
    }}
    if website == '' or password == '':
        messagebox.showerror(title="Oops", message="Please don't leave and fields empty")
    else:
        try:
            with open("my_pws.json", 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("my_pws.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("my_pws.json", 'w') as file:
                data.update(new_data)
                json.dump(data, file, indent=4)

        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", padx=10)
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", padx=10)
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", padx=10)
password_label.grid(row=3, column=0)

website_input = Entry()
website_input.grid(row=1, column=1, sticky="EW")
website_input.focus()
email_input = Entry()
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
email_input.insert(0, STANDARD_EMAIL)
password_input = Entry()
password_input.grid(row=3, column=1, sticky="EW")

search_btn = Button(text="Search", width=15, command=search)
search_btn.grid(row=1, column=2)

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=35, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
