from car import Car
# STARTING_MOVE_DISTANCE = 5
STARTING_MOVE_DISTANCE = 35
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        super().__init__()
        self.cars = []

    def add_car(self):
        new_car = Car()
        self.cars.append(new_car)

    def move_cars(self):
        for index, car in enumerate(self.cars):
            car.forward(STARTING_MOVE_DISTANCE)
            print(car)
            if car.xcor() < -260:
                self.cars.pop(index)
                # car stays on screen even after deleting it, so hide it first.
                car.hideturtle()
                del car
