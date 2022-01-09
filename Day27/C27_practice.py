import tkinter

window = tkinter.Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="Welcome to this program", font=('Arial', 24, 'bold'))
my_label.pack()

#*args

def add(*args):
    result = 0
    for num in args:
        result += num
    print(result)

add(5,4,5,6,7)



window.mainloop()