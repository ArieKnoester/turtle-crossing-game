from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)
        # I'm not sure if this is the best place to check if the player has
        # crossed the finish line. Both the scoreboard and car_manager will
        # need to see this event.
        if self.reached_finish_line:
            self.goto(STARTING_POSITION)

    @property
    def reached_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y
