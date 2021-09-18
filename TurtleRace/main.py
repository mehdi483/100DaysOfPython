from turtle import Turtle, Screen
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
s = Screen()


def create_turtle(turtle_color):
    t = Turtle("turtle")
    t.color(turtle_color)
    return t


def create_turtles(color_list):
    if len(color_list) > 8:
        return

    turtle_list = []
    for color in color_list:
        t = create_turtle(color)
        t.penup()
        turtle_list.append(t)

    return turtle_list


def arrange_turtles(turtle_list):
    x = -s.window_width() // 2 + 30
    y = -(len(turtle_list) - 1) * 50 // 2

    for t in turtle_list:
        t.goto(x, y)
        y += 50


def move_turtle(t):
    t.forward(randint(5, 10))


def move_turtles(turtle_list):
    for t in turtle_list:
        move_turtle(t)


def check_winner(turtle_list):
    finish_line = s.window_width() // 2 - 30
    winner = None
    winner_xcor = 0

    for t in turtle_list:
        xcor = t.xcor()
        if xcor >= finish_line and xcor >= winner_xcor:
            winner = t
            winner_xcor = xcor

    return winner


def print_banner(banner_text):
    banner = Turtle()
    banner.penup()
    banner.color("black")
    banner.write(banner_text, False, "center", ("Arial", 14, "normal"))


def play():
    turtles = create_turtles(COLORS)
    arrange_turtles(turtles)

    chosen_winner = s.textinput("Lucky Guess", "Which color going to win?").strip().lower()
    while chosen_winner not in COLORS:
        chosen_winner = s.textinput("Lucky Guess", "No racer with that color. Guess again.").strip().lower()

    game_is_over = False
    while not game_is_over:
        move_turtles(turtles)
        winner = check_winner(turtles)
        if winner is not None:
            game_is_over = True

    if winner.fillcolor() == chosen_winner:
        print_banner(f"{winner.fillcolor().capitalize()} racer won! You guessed right!")
    else:
        print_banner(f"{winner.fillcolor().capitalize()} won! You guessed wrong :(")


play()
s.exitonclick()
