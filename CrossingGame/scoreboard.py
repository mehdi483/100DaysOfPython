from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-260, 260)
        self.print_level()

    def print_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.print_level()

    def game_over(self):
        self.goto(50, 260)
        self.write("GAME OVER!", font=FONT)


