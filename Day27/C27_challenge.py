from tkinter import *

window = Tk()
window.title('SEK to EURO Converter')
window.minsize(width=300, height=150)
window.config(padx=30, pady=30)

def calculate():
    sum_sek = float(number_input.get())
    result = round(sum_sek * 0.097, 2)
    result_label.config(text=result)


label_is_equal = Label(text="is equal to")
label_is_equal.grid(row=1, column=0, padx=2, pady=2)

number_input = Entry()
number_input.insert(END, '0')
number_input.grid(row=0, column=1, padx=2, pady=2)

label_sek = Label(text="SEK")
label_sek.grid(row=0, column=2, padx=2, pady=2)

result_label = Label(text=0)
result_label.grid(row=1, column=1, padx=2, pady=2)

label_eur = Label(text='EUR')
label_eur.grid(row=1, column=2, padx=2, pady=2)

button = Button(text='Calculate', command=calculate)
button.grid(row=2, column=1,padx=2, pady=2)
window.mainloop()
