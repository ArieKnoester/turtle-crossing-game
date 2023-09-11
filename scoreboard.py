from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=255)
        self.display_level(player_level=1)

    def display_level(self, player_level):
        self.clear()
        self.write(
            f"Level: {player_level}", font=FONT)
