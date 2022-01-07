from turtle import Turtle

TEXT_START_POSITION = (0, 260)
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(TEXT_START_POSITION)
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.goto(TEXT_START_POSITION)
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)

    def start_game(self):
        self.goto(-80, -280)
        self.write('Press space to start the game')

    def clear_start_game(self):
        self.clear()
        self.write_score()
