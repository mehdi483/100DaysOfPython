from turtle import Turtle

WIDTH_FACTOR = 5
LENGTH_FACTOR = 1
STEPS = 10
LEFT_PAD_XCOR = -350
RIGHT_PAD_XCOR = 350


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()

        if side.lower() == "left":
            self.setx(LEFT_PAD_XCOR)
        elif side.lower() == "right":
            self.setx(RIGHT_PAD_XCOR)
        else:
            return

        self.side = side

        self.penup()
        self.speed("fastest")
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=WIDTH_FACTOR, stretch_len=LENGTH_FACTOR)
        print(f"{self.side.capitalize()} paddle's current position is {self.position()}.")

    def get_bottom_cor(self):
        ycor = self.ycor() - 50

        if self.side == "left":
            xcor = self.xcor() + 10
        else:
            xcor = self.xcor() - 10

        return xcor, ycor

    def get_top_cor(self):
        ycor = self.ycor() + 50

        if self.side == "left":
            xcor = self.xcor() + 10
        else:
            xcor = self.xcor() - 10

        return xcor, ycor

    def move_up(self):
        if self.get_top_cor()[1] < 300:
            self.goto(self.xcor(), self.ycor() + STEPS)
            print(f"{self.side.capitalize()} paddle is moving up.")
        print(f"{self.side.capitalize()} paddle's current position is {self.position()}.")

    def move_down(self):
        if self.get_bottom_cor()[1] > -290:
            self.goto(self.xcor(), self.ycor() - STEPS)
            print(f"{self.side.capitalize()} paddle is moving down.")
        print(f"{self.side.capitalize()} paddle's current position is {self.position()}.")
