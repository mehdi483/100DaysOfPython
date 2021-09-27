import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()
screen.listen()
screen.onkeypress(player.cross, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.run()

    if cars.does_collide(player):
        game_is_on = False
        scoreboard.game_over()
        screen.onkeypress(None, "Up")

    if player.crossed_finish_line():
        scoreboard.level_up()
        cars.speed_up()
        player.go_to_start()

    screen.update()

screen.exitonclick()
