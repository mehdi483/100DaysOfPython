from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, side):
        super().__init__()
        self.side = side
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")

        if self.side == "left":
            self.goto(-100, 180)
        elif self.side == "right":
            self.goto(100, 180)
        else:
            return

        self.print_score()

    def print_score(self):
        self.clear()
        self.write(self.score, align="center", font=("courier", 80, "normal"))

    def add_score(self):
        self.score += 1
        self.print_score()
