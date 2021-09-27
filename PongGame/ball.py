from turtle import Turtle
from random import choice

HEADINGS = [45, 135, 225, 315]
STEPS = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(choice(HEADINGS))
        self.ball_speed = 0.01

    def move(self):
        self.forward(STEPS)

    def reset_position(self):
        self.goto(0, 0)
        self.reflect_paddle()
        self.ball_speed = 0.01

    def reflect_screen(self):
        new_heading = 360 - self.heading()
        self.setheading(new_heading)

    def reflect_paddle(self):
        cur_heading = self.heading()
        if cur_heading in [45, 225]:
            self.setheading(cur_heading + 90)
        elif self.heading() in [135, 315]:
            self.setheading(cur_heading - 90)

        self.ball_speed *= 0.9
