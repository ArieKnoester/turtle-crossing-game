from car import Car
import random
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self, player):
        super().__init__()
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.player = player

    def create_car_randomly(self):
        # 1 in 4 chance of creating a car. Keeps the density of cars
        # low enough to give the player a chance of succeeding.
        can_add_car = random.choice(("y", "n", "n", "n"))
        if can_add_car == "y":
            self.add_car()

    def add_car(self):
        new_car = Car()
        self.cars.append(new_car)

    def move_cars(self):
        for index, car in enumerate(self.cars):
            car.forward(self.move_distance)
            if self.car_collision(car):
                return False
            if car.off_screen:
                self.cars.pop(index)
                # car remains visible even after deleting it, so hide it first.
                car.hideturtle()
                del car
        return True

    def car_collision(self, car):
        if (
            (car.xcor() - 20 < self.player.xcor() < car.xcor() + 20)
            and
            (car.ycor() - 15 < self.player.ycor() < car.ycor() + 15)
        ):
            return True
        return False

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
