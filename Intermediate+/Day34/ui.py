import time
from tkinter import *
from quiz_model import Quiz

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_model: Quiz):
        self.quiz = quiz_model
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.right_img = PhotoImage(file='images/true.png')
        self.wrong_img = PhotoImage(file='images/false.png')

        self.score = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=300, bg='white')
        self.question = self.canvas.create_text(150, 150, text='Question', font=('Arial', 20, 'italic'),
                                                fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50, padx=20)

        self.right_btn = Button(image=self.right_img, borderwidth=0, bg=THEME_COLOR, command=self.true_pressed)
        self.wrong_btn = Button(image=self.wrong_img, borderwidth=0, bg=THEME_COLOR, command=self.false_pressed)
        self.right_btn.grid(row=2, column=0)
        self.wrong_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of the quiz")
            self.right_btn.config(state='disabled')
            self.wrong_btn.config(state='disabled')

    def true_pressed(self):
        is_right = self.quiz.check_answer('true')
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('false')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            print("in is right")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question())
