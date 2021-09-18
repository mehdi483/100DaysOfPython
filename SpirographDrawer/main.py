from turtle import Turtle, Screen, colormode
from random import randint, choice


colormode(255)


def random_color():
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    return color


def draw_spirogrpah(turtle, circle_radius, gap_size):
    for angle in range(0, 360, gap_size):
        turtle.setheading(angle)
        turtle.color(random_color())
        turtle.circle(circle_radius)


t = Turtle()
t.speed(0)
draw_spirogrpah(t, 150, 4)

s = Screen()
s.exitonclick()
