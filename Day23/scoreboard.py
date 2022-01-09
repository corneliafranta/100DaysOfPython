from turtle import Turtle

FONT = ("Courier", 24, "normal")
GAMEOVER_FONT = ('Courier', 24, 'bold')
LEVEL_DISPLAY_POS = (-280, 260)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(LEVEL_DISPLAY_POS)

    def increase_level(self):
        self.level += 1

    def display_level(self):
        self.clear()
        self.goto(LEVEL_DISPLAY_POS)
        self.write(f'Level: {self.level}', font=FONT, align='left')

    def game_over(self):
        self.home()
        self.write(f'GAME OVER', font=GAMEOVER_FONT, align='center')
