from time import sleep
from turtle import Screen

from Day21.ball import Ball
from Day21.paddle import Paddle
from Day21.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('My Pong Game')
screen.tracer(0)

right_paddle = Paddle(screen, 'right')
left_paddle = Paddle(screen, 'left')
ball = Ball()
scoreboard = Scoreboard()
scoreboard.write_score()
screen.update()
sleep(0.01)
screen.listen()
screen.onkeypress(right_paddle.move_up, 'Up')
screen.onkeypress(right_paddle.move_down, 'Down')
screen.onkeypress(left_paddle.move_up, 'w')
screen.onkeypress(left_paddle.move_down, 's')
game_is_on = True

while game_is_on:
    ball.move()

    # detect collision top, bottom

    print(ball.ycor())
    if ball.hit_upper_wall() or ball.hit_lower_wall():
        ball.bounce_y()
        print("hit wall")

    if ball.hit_right_wall():
        scoreboard.increase_score('l')
        ball.reset_position()

    if ball.hit_left_wall():
        scoreboard.increase_score('r')
        ball.reset_position()

    # detect collision with paddles

    if ball.hit_right_paddle(right_paddle.paddle) or ball.hit_left_paddle(left_paddle.paddle):
        ball.bounce_x()

    screen.update()
    print(ball.current_speed)
    sleep(ball.current_speed)

screen.exitonclick()
