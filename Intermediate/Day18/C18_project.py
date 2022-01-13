import turtle
from turtle import Turtle, Screen
import random
import colorgram

def extract_colors(image, amount):
    colors = []
    extracted_colors = colorgram.extract(image, amount)
    for color in extracted_colors:
        color_1 = tuple(color.rgb)
        colors.append(color_1)

    return colors

turtle.colormode(255)
colors = [(211, 154, 98), (53, 107, 131), (235, 240, 244), (177, 78, 33), (198, 142, 35), (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130), (190, 88, 109), (12, 50, 64), (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (224, 93, 79), (243, 163, 161), (38, 32, 34), (3, 25, 25), (80, 147, 169), (161, 26, 22), (21, 78, 90), (234, 167, 171), (171, 206, 190), (103, 127, 156), (165, 202, 210)]
emelie = Turtle()
emelie.shape('turtle')
emelie.speed(0)
emelie.penup()
emelie.hideturtle()
emelie.setheading(225)
emelie.forward(300)
emelie.setheading(0)

number_of_dots = 100


def draw_dot_painting(number_dots):
    for dot_count in range(1, number_dots +1):
        emelie.dot(20, random.choice(colors))
        emelie.forward(50)

        if dot_count % 10 == 0:
            emelie.setheading(90)
            emelie.forward(50)
            emelie.setheading(180)
            emelie.forward(500)
            emelie.setheading(0)


draw_dot_painting(100)

screen = Screen()
screen.exitonclick()