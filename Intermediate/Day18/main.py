import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return(r, g, b)


timmy = Turtle()
timmy.shape('turtle')
timmy.color('chartreuse2')


# Exercise 1
def draw_square(size):
    for i in range(4):
        timmy.forward(size)
        timmy.right(90)


# Exercise 2
def draw_dashed_line(size):
    for i in range(size):
        if not i % 2 == 0:
            timmy.forward(10)
            timmy.penup()
        else:
            timmy.forward(10)
            timmy.pendown()


# Bonus Exercise
def draw_dashed_square(size):
    for i in range(4):
        draw_dashed_line(size)
        timmy.right(90)

#Exercise 3
def draw_shape(number_sides):
    angle = 360 / number_sides
    for i in range(number_sides):
        timmy.forward(100)
        timmy.right(angle)

def draw_pattern(amount_shapes):
    for i in range(amount_shapes):
        timmy.pencolor(random_color())
        draw_shape(i + 3)


#Exercise 4
def draw_random_walk(lenght, step_lenght):
    angles=[0, 90, 180, 270]
    timmy.pensize(3)
    timmy.speed('fastest')
    for i in range(lenght):
        timmy.pencolor(random_color())
        timmy.forward(step_lenght)
        timmy.setheading(random.choice(angles))



def draw_sqirograph(size_of_gap):
    for i in range (int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)




draw_sqirograph(50)

screen = Screen()
screen.exitonclick()
