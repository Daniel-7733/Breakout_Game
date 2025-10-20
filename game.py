import turtle
import time
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
        self.game_font: tuple[str, int, str] = ("font/Pixeltype.ttf", 16, "bold") # Font is not working

        self.screen.screensize(400, 300, self.BACKGROUND)
        self.ga.title("Breakout Game")
        # self.ga.Screen().bgcolor(self.BACKGROUND)

        self.text_writer(text="Score: {Add The score}", align="left", x=-360, y=310)
        self.text_writer(text="00:00:00", align="right", x=280, y=310) # I should connect my function to timer
        self.ga.hideturtle() # this one remove the turtle after drawing

        self.player: Player = Player()
        self.brick: Brick = Brick()
        self.ball: Ball = Ball()
        self.ball.set_paddle(self.player.player)  # Pass the actual turtle of the paddle

        self.ball.constant_movement()

        self.ga.done() # This one will come after self.ga.hideturtle()
        self.ga.mainloop()

    def text_writer(self, text: str, align: str, x: int, y: int) -> None:
        self.ga.color(self.main_color)
        self.ga.penup()
        self.ga.goto(x, y)
        self.ga.write(text, align=align, font=self.game_font)


    def game_timer(self):
        # TODO: two problems:
              # todo 1: timer is current timer and it is not a timer
              # todo 2: timer's refresh if too high which is like a fast blinking.
        while True:
            self.ga.clear()  # This one clean the previous timer (00:00:00)
            current_time: float = time.time()
            local_time = time.localtime(current_time)

            minute = local_time.tm_min
            second = local_time.tm_sec
            microsecond: int = int((current_time - int(current_time)) * 1000000)
            self.text_writer(text=f"{minute}:{second}:{microsecond}", align="right", x=280, y=310)

            self.screen.ontimer(self.game_timer, 1000)


    # def game_border(self) -> None:
    #     self.ga.speed(300)
    #     self.ga.penup()
    #     self.ga.goto(-420, -400)
    #     self.ga.pendown()
    #     self.ga.color(self.main_color)
    #
    #     self.ga.left(90)
    #     for i in range(2):
    #         self.ga.forward(770)
    #         self.ga.right(90)
    #         self.ga.forward(840)
    #         self.ga.right(90)
