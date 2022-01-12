import random
import time

import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
data = {}
current_word = {}
# ----------------------------------- Data ---------------------------------------------#
try:
    data = pandas.read_csv("data/words_to_learn")

except FileNotFoundError:
    data = pandas.read_csv('data/swe_eng - swe_eng.csv').to_dict(orient='records')
else:
    data = data.to_dict(orient='records')




def show_new_card():
    global current_word, flip_timer
    card = random.choice(data)
    current_word = card
    window.after_cancel(flip_timer)
    canvas.itemconfig(subheader, text="Swedish", fill="black")
    canvas.itemconfig(word_swe, text=card['swe'], fill="black")
    canvas.itemconfig(canvas_image, image=flashcard_front )
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(subheader, text="English", fill="white")
    canvas.itemconfig(word_swe, text=current_word['en'], fill="white")
    canvas.itemconfig(canvas_image, image=flashcard_back)


def knows_card():
    data.remove(current_word)
    to_learn = pandas.DataFrame(data)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    show_new_card()


# ----------------------------------- UI ---------------------------------------------#
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title('Flashy')
window.after(3000, func=flip_card)
flip_timer = window.after(3000, func=flip_card)
# Images
flashcard_front = PhotoImage(file="images/card_front.png")
flashcard_back = PhotoImage(file="images/card_back.png")
wrong_btn_image = PhotoImage(file="images/wrong.png")
right_btn_image = PhotoImage(file="images/right.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=flashcard_front)
word_swe = canvas.create_text(400, 263, text="Hej", font=(FONT_NAME, 60, 'bold'))
subheader = canvas.create_text(400, 150, text="Swedish", font=(FONT_NAME, 40, 'italic'))
canvas.grid(row=0, column=0, columnspan=2)

wrong_btn = Button(image=wrong_btn_image, highlightthickness=0, borderwidth=0, command=show_new_card)
wrong_btn.grid(row=1, column=0)

right_btn = Button(image=right_btn_image, highlightthickness=0, borderwidth=0, command=knows_card)
right_btn.grid(row=1, column=1)

show_new_card()

window.mainloop()
