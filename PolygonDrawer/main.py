from turtle import Turtle, Screen
from random import random


def draw(turtle, edge_count, edge_length):
    if edge_count < 3:
        return

    color = random_color()
    turtle.color(color["r"], color["g"], color["b"])
    right_turn_angle = 360 / edge_count

    for _ in range(edge_count):
        turtle.right(right_turn_angle)
        turtle.forward(edge_length)


def random_color():
    return {"r": random(), "b": random(), "g": random()}


t = Turtle()
for edges in range(3, 11):
    print(edges)
    draw(t, edges, 100)


s = Screen()
s.exitonclick()
