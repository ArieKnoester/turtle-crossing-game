from car import Car
import random
STARTING_MOVE_DISTANCE = 5
# STARTING_MOVE_DISTANCE = 35 # for testing
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        super().__init__()
        self.cars = []

    def create_car_randomly(self):
        # 1 in 4 chance of creating a car. Keeps the density of cars
        # low enough to give the player a fair chance of succeeding.
        can_add_car = random.choice(("y", "n", "n", "n"))
        if can_add_car == "y":
            self.add_car()

    def add_car(self):
        new_car = Car()
        self.cars.append(new_car)

    def move_cars(self):
        for index, car in enumerate(self.cars):
            car.forward(STARTING_MOVE_DISTANCE)
            if car.off_screen:
                self.cars.pop(index)
                # car remains visible even after deleting it, so hide it first.
                car.hideturtle()
                del car
