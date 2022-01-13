import random
from turtle import Turtle


def create_random_coordinates():
    x = random.randint(-270, 270)
    y = random.randint(-270, 270)
    return (x, y)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.goto(create_random_coordinates())

    def refresh(self):
        coordinates = create_random_coordinates()
        self.goto(coordinates)
