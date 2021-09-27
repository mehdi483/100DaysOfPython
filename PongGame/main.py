from turtle import Screen
from ball import Ball
from player import Player
from time import sleep

s = Screen()

s.title("Pong")
s.bgcolor("black")
s.setup(800, 600)
s.tracer(0)

ball = Ball()
player_left = Player("left")
player_right = Player("right")

s.listen()
s.onkeypress(player_left.move_up, "w")
s.onkeypress(player_left.move_down, "s")
s.onkeypress(player_right.move_up, "Up")
s.onkeypress(player_right.move_down, "Down")


while True:
    sleep(ball.ball_speed)
    s.update()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.reflect_screen()
    elif ball.xcor() >= 380:
        player_right.add_score()
        ball.reset_position()
    elif ball.xcor() <= -380:
        player_left.add_score()
        ball.reset_position()
    elif ball.ycor() - 10 <= player_left.get_top_cor()[1] and ball.ycor() + 10 >= player_left.get_bottom_cor()[1] and ball.xcor() - player_left.xcor() <= 20:
        ball.reflect_paddle()
    elif ball.ycor() - 10 <= player_right.get_top_cor()[1] and ball.ycor() + 10 >= player_right.get_bottom_cor()[1] and player_right.xcor() - ball.xcor() <= 20:
        ball.reflect_paddle()
