import time
from turtle import Screen
from player import Player


def initialize_screen():
    new_screen = Screen()
    new_screen.setup(width=600, height=600)
    new_screen.tracer(0)
    new_screen.listen()
    return new_screen


screen = initialize_screen()
player = Player()
screen.onkey(fun=player.up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    player.car_manager.create_car_randomly()
    player.car_manager.move_cars()
