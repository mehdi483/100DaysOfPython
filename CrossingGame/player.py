from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def cross(self):
        self.forward(MOVE_DISTANCE)

    def crossed_finish_line(self):
        if FINISH_LINE_Y - self.ycor() < 10:
            return True
        else:
            return False
