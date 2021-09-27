import random
from turtle import Turtle
from random import choice, randrange, random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.speed = 5
        self.initiate_cars()

    def create_car(self):
        car = Turtle("square")
        car.penup()
        car.color(choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setheading(180)
        car.goto(320, randrange(-250, 250))
        self.car_list.append(car)

    def initiate_cars(self):
        prob = random()

        if prob > 0.7:
            self.create_car()

    def run(self):
        for car in self.car_list:
            if car.xcor() <= -320:
                self.car_list.remove(car)
            else:
                car.forward(self.speed)

        self.initiate_cars()

    def speed_up(self):
        self.speed += MOVE_INCREMENT

    def does_collide(self, colliding_turtle):
        t_right_x = colliding_turtle.xcor() + 10 * colliding_turtle.shapesize()[1]
        t_left_x = colliding_turtle.xcor() - 10 * colliding_turtle.shapesize()[1]
        t_top_y = colliding_turtle.ycor() + 10 * colliding_turtle.shapesize()[0]
        t_bottom_y = colliding_turtle.ycor() - 10 * colliding_turtle.shapesize()[0]

        for car in self.car_list:
            c_right_x = car.xcor() + 20
            c_left_x = car.xcor() - 20
            c_top_y = car.ycor() + 10
            c_bottom_y = car.ycor() - 10
            if t_right_x >= c_left_x and t_left_x <= c_right_x and t_top_y >= c_bottom_y and t_bottom_y <= c_top_y:
                return True

        return False
