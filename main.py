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

# Returns false if a car hits a turtle
while player.car_manager.move_cars():
    time.sleep(0.1)
    screen.update()
    player.car_manager.create_car_randomly()
    player.car_manager.move_cars()

# Loop immediately stops when a car hits a turtle.
# At higher car speeds the loop will stop just before
# the player sees the collision. Update the screen again
# after exiting the loop, so the collision is visible.
screen.update()
screen.exitonclick()
