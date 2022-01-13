from turtle import Turtle

TEXT_START_POSITION = (0, 260)
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.high_score = self.get_highscore()
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
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)



    def start_game(self):
        self.goto(-80, -280)
        self.write('Press space to start the game')

    def clear_start_game(self):
        self.clear()
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.write_score()


    def get_highscore(self):
        with open('data.txt') as file:
            high_score = int(file.read())
            print(high_score)
            return high_score

    def update_high_score(self):
        with open('data.txt', 'w') as file:
            file.write(str(self.high_score))