import time
from turtle import Screen
from player import Player
from car_manager import CarManager


def initialize_screen():
    new_screen = Screen()
    new_screen.setup(width=600, height=600)
    new_screen.tracer(0)
    new_screen.listen()
    return new_screen


screen = initialize_screen()
player = Player()
car_manager = CarManager()
car_manager.add_car()
screen.onkey(fun=player.up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
