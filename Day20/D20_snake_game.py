from turtle import Screen

from Day20.food import Food
from Day20.scoreboard import Scoreboard
from Day20.snake import Snake

game_is_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake(screen)
food = Food()
scoreboard = Scoreboard()


def game_play():
    global game_is_on
    scoreboard.clear_start_game()
    while game_is_on:

        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            scoreboard.increase_score()
            snake.extend_snake()
            food.refresh()

        # Detect collision with wall
        if any([hit_right_wall(), hit_left_wall(), hit_upper_wall(), hit_lower_wall()]):
            game_is_on = False

        # Detect collision with tail
        for segment in snake.snake[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    scoreboard.game_over()


screen.update()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(game_play, 'space')


def hit_left_wall():
    return snake.head.xcor() < -280


def hit_right_wall():
    return snake.head.xcor() > 280


def hit_upper_wall():
    return snake.head.ycor() > 280


def hit_lower_wall():
    return snake.head.ycor() < -280


scoreboard.start_game()

screen.exitonclick()
