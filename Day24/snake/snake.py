import time
from turtle import Turtle

STARTING_POSITION = [(0.00, 0.00), (-20.00, 0.00), (-40.00, 0.00)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, screen):
        self.snake_length = 3
        self.snake = []
        self.create_snake()
        self.screen = screen
        self.direction = 0
        self.head = self.snake[0]

    def create_snake_part(self, position):
        snake_body_part = Turtle(shape='square')
        snake_body_part.penup()
        snake_body_part.color('white')
        snake_body_part.goto(position)
        self.snake.append(snake_body_part)
        return snake_body_part

    def create_snake(self):
        snake = []
        for coordinate in STARTING_POSITION:
            snake_body_part = self.create_snake_part(coordinate)

            snake.append(snake_body_part)
        return snake

    def extend_snake(self):
        x = self.snake[-1].xcor() - 20
        y = self.snake[-1].ycor()
        new_body_part = self.create_snake_part((x, y))

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.setheading(self.direction)
        self.head.forward(MOVE_DISTANCE)

        self.screen.update()
        time.sleep(0.1)

    def up(self):
        if self.direction is not DOWN:
            self.direction = UP

    def down(self):
        if self.direction is not UP:
            self.direction = DOWN

    def left(self):
        if self.direction is not RIGHT:
            self.direction = LEFT

    def right(self):
        if self.direction is not LEFT:
            self.direction = RIGHT

    def reset(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.snake = self.create_snake()
        self.head = self.snake[0]