from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=255)
        self.player_level = 1
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(
            f"Level: {self.player_level}", font=FONT)
