import turtle
from player import Player
from ball import Ball
from brick import Brick


class Game:
    def __init__(self) -> None:
        self.ga = turtle
        self.BACKGROUND: str = "#221824"

        self.ga.title("Breakout Game")
        self.ga.Screen().bgcolor(self.BACKGROUND)

        self.player = Player()
        self.ball = Ball()
        self.brick = Brick()

        self.ball.constant_movement()

        self.ga.mainloop()
