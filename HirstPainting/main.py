from turtle import Turtle, Screen, colormode
from random import choice
from colors import COLORS


def draw_row(turtle, direction, column_count, dot_diameter):
    turtle.setheading(direction)

    for i in range(column_count):
        t.dot(dot_diameter, choice(COLORS))
        if i < column_count - 1:
            t.forward(dot_diameter * 2)


def go_up(turtle, dot_diameter):
    turtle.setheading(90)
    turtle.forward(dot_diameter * 2)


def draw_hirst(turtle, row_count, column_count, dot_diameter):
    direction = 0
    turtle.penup()
    turtle.hideturtle()

    for _ in range(row_count):
        draw_row(turtle, direction, column_count, dot_diameter)
        go_up(turtle, dot_diameter)
        direction = (direction + 180) % 360


colormode(255)
t = Turtle()
draw_hirst(t, 10, 10, 20)


s = Screen()
s.exitonclick()
