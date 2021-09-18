from turtle import Turtle, Screen
from random import choice, random


def random_walk(turtle, steps):
    color = random_color()
    turtle.color(color["r"], color["g"], color["b"])

    direction = random_angle()
    turtle.setheading(direction)

    turtle.forward(steps)


def random_color():
    return {"r": random(), "b": random(), "g": random()}


def random_angle():
    return choice([0, 90, 180, 270])


t = Turtle()
t.width(10)

for _ in range(200):
    random_walk(t, 20)


s = Screen()
s.exitonclick()
