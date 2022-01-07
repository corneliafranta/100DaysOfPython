from turtle import Turtle

LEFT_SCORE_POSITION = (-100, 200)
RIGHT_SCORE_POSITION = (100, 200)
ALIGNMENT = 'center'
FONT = ('Courier', 70, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.l_score = 0
        self.r_score = 0

    def increase_score(self, player):
        self.clear()
        if player == 'l':
            self.l_score += 1
        else:
            self.r_score += 1
        self.write_score()

    def write_score(self):
        self.goto(LEFT_SCORE_POSITION)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(RIGHT_SCORE_POSITION)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)

    def start_game(self):
        self.goto(-80, -280)
        self.write('Press space to start the game')

    def clear_start_game(self):
        self.clear()
        self.write_score()
