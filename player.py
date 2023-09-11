from turtle import Turtle
from scoreboard import Scoreboard
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self, scoreboard):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.level = 1
        self.scoreboard = scoreboard

    def up(self):
        self.forward(MOVE_DISTANCE)
        if self.reached_finish_line:
            self.level += 1
            self.scoreboard.display_level(player_level=self.level)
            self.goto(STARTING_POSITION)

    @property
    def reached_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
