import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

game_is_on = True
player = Player(screen)
scoreboard = Scoreboard()
car_manager = CarManager(scoreboard)

screen.onkey(player.move_forward, 'Up')

while game_is_on:
    scoreboard.display_level()
    car_manager.create_car()
    car_manager.move()
    time.sleep(0.1)
    screen.update()
    for car in car_manager.cars:
        did_collied = player.check_for_collision(car)
        if did_collied:
            print('collision')
            game_is_on = False
            scoreboard.game_over()
    if player.reached_goal():
        player.reset_position()
        scoreboard.increase_level()

screen.exitonclick()
