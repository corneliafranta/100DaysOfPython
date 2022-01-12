from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.right_img = PhotoImage(file='images/true.png')
        self.wrong_img = PhotoImage(file='images/false.png')

        self.score = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1)


        self.canvas = Canvas(width=300, height=300, bg='white')
        self.question = self.canvas.create_text(150, 150, text='Question', font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20, padx=20)

        self.right_btn = Button(image=self.right_img, borderwidth=0, bg=THEME_COLOR)
        self.wrong_btn = Button(image=self.wrong_img, borderwidth=0, bg=THEME_COLOR)
        self.right_btn.grid(row=2, column=0)
        self.wrong_btn.grid(row=2, column=1)

        self.window.mainloop()
