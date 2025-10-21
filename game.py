import turtle
from time import sleep
from turtle import Screen
from player import Player
from ball import Ball
from brick import Brick


class Game:
    def __init__(self) -> None:
        self.ga = turtle
        self.screen = Screen()
        self.BACKGROUND: str = "#221824"
        self.main_color: str = "#FF7B00"
        self.game_font: tuple[str, int, str] = ("Pixeltype", 20, "bold") # Font is not working

        self.screen.screensize(400, 300, self.BACKGROUND)
        self.ga.title("Breakout Game")

        self.writer = turtle.Turtle()
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.color(self.main_color)

        self.text_writer(text="Score: 0", align="left", x=-360, y=310)

        self.player: Player = Player()
        self.brick: Brick = Brick()
        self.ball: Ball = Ball()
        self.ball.set_paddle(self.player.player)  # Pass the actual turtle of the paddle

        self.ball.constant_movement()

        self.ga.mainloop()

    def text_writer(self, text: str, align: str, x: int, y: int) -> None:
        self.writer.goto(x, y)
        self.writer.clear()
        self.writer.write(text, align=align, font=self.game_font)


    def game_timer(self) -> None: # I don't think I will use this function because the while loop will interrupt the game loop
        """This function will count time from millisecond to minutes"""
        millisecond: int = 0
        second: int = 0
        minute: int = 0
        timer: str = f"{minute:02}:{second:02}:{millisecond:02}"

        while True:
            sleep(0.001)
            if minute >= 3:
                print("A chicken can do better then you")

            self.text_writer(text=timer, align="right", x=280, y=310)
            millisecond += 1

            if millisecond == 1000:
                second += 1
                millisecond = 0
            if second == 60:
                minute += 1
                second = 0


    def game_border(self) -> None:
        """Drawing the game border"""
        self.ga.speed(300)
        self.ga.penup()
        self.ga.goto(-420, -400)
        self.ga.pendown()
        self.ga.color(self.main_color)

        self.ga.left(90)
        for i in range(2):
            self.ga.forward(770)
            self.ga.right(90)
            self.ga.forward(840)
            self.ga.right(90)
