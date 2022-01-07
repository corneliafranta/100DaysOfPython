import time
from turtle import Turtle

STARTING_POSITION_RIGHT = (350, 0)
STARTING_POSITION_LEFT = (-350, 0)
STEP = 20


class Paddle:
    def __init__(self, screen, side):
        self.screen = screen
        self.side = side
        self.paddle = self.create_paddle(side)

    def create_paddle(self, side):
        if side == 'left':
            starting_pos = STARTING_POSITION_LEFT
        else:
            starting_pos = STARTING_POSITION_RIGHT
        pad = Turtle('square')
        pad.penup()
        pad.color('white')
        pad.shapesize(stretch_wid=5, stretch_len=1)
        pad.goto(starting_pos)
        self.screen.update()
        time.sleep(0.1)
        return pad

    def move_up(self):
        current_x = self.paddle.xcor()
        current_y = self.paddle.ycor()
        self.paddle.goto(current_x, current_y + 20)
        self.screen.update()
        time.sleep(0.01)

    def move_down(self):
        current_x = self.paddle.xcor()
        current_y = self.paddle.ycor()
        self.paddle.goto(current_x, current_y - 20)
        self.screen.update()
        time.sleep(0.01)
