from turtle import Turtle

INITIAL_COR = [(0, 0), (-20, 0), (-40, 0)]
STEP_LEN = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.should_grow = False

        self.tiles = []
        for cor in INITIAL_COR:
            self.grow(cor)

        self.head = self.tiles[0]

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move(self):
        tail_cor = self.tiles[-1].position()

        for i in range(len(self.tiles) - 1, 0, -1):
            self.tiles[i].goto(self.tiles[i - 1].position())

        if self.should_grow:
            self.grow(tail_cor)
            self.should_grow = False

        self.head.forward(STEP_LEN)

    def grow(self, cor):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(cor)
        self.tiles.append(t)

    def is_head_tail_colliding(self):
        for current_tile in self.tiles[1:]:
            if self.head.distance(current_tile) < 10:
                return True

        return False
