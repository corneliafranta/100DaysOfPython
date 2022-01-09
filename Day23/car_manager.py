import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
EASY = [1]
MEDIUM = [1, 3]
HARD =[1,3,5]



class CarManager:
    def __init__(self, scoreboard):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.level = EASY
        self.scoreboard = scoreboard

    def create_car(self):
        random_choice = random.randint(1, 6)
        if random_choice in self.level:
            car = Turtle('square')
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(stretch_len=1, stretch_wid=2)
            pos_y = random.randint(-250, 250)
            car.goto(300,pos_y)
            car.right(90)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            new_x = car.xcor() - self.car_speed
            new_y = car.ycor()
            car.goto(new_x, new_y)

    def set_difficulty(self):
        self.car_speed += MOVE_INCREMENT
        if self.scoreboard.level == 5:
            self.level = MEDIUM
        elif self.scoreboard.level == 10:
            self.level = HARD

