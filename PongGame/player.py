from paddle import Paddle
from scoreboard import Scoreboard


class Player(Paddle):
    def __init__(self, side):
        super().__init__(side)
        self.score = Scoreboard(side)

    def add_score(self):
        self.score.add_score()
        print(f"{self.side.capitalize()} player's score is: {self.score.score}")
