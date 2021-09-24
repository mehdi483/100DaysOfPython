from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
scores = Scoreboard()

s.listen()
s.onkey(snake.go_up, "Up")
s.onkey(snake.go_down, "Down")
s.onkey(snake.go_right, "Right")
s.onkey(snake.go_left, "Left")


game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.should_grow = True
        scores.add_point()

    if snake.head.xcor() >= 280 or snake.head.xcor() <= -280 or snake.head.ycor() >= 280 or snake.head.ycor() <= -280:
        game_is_on = False
        scores.game_over()
    elif snake.is_head_tail_colliding():
        game_is_on = False
        scores.game_over()


s.exitonclick()
