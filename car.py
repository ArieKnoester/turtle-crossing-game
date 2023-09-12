from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        car_color = random.choice(COLORS)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(car_color)
        self.setheading(180)
        self.hideturtle()
        self.penup()
        random_ycor = random.randrange(-280, 280)
        self.goto(x=280, y=random_ycor)
        self.showturtle()
