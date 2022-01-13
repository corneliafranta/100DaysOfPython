import turtle
from time import sleep
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
        self.screen = screen

    def move_forward(self):
        self.forward(10)
        self.screen.update()
        sleep(0.1)

    def check_for_collision(self, object):
        return self.distance(object) < 25

    def reached_goal(self):
        return self.ycor() > 300

    def reset_position(self):
        self.goto(STARTING_POSITION)