from turtle import Turtle


class Player:
    def __init__(self) -> None:
        self.player = Turtle()
        self.PLAYER_COLOR: str = "#eef074"
        self.PLAYER_SPEED: int = 100
        self.player.speed(20)
        self.draw_racket()

        self.player.screen.onkey(self.move_left, "Left")
        self.player.screen.onkey(self.move_right, "Right")
        self.player.screen.listen()

    def draw_racket(self) -> None:
        """Here I use turtle itself to make the rectangle"""
        self.player.shape("square")
        self.player.color(self.PLAYER_COLOR)
        self.player.penup()
        self.player.setpos(0, -300)
        self.player.shapesize(stretch_wid=1, stretch_len=5)  # 10px height, 50px width

    def move_left(self) -> None:
        """Here the function receive the x coordinate & and then we subtract 20 from it."""
        self.player.penup()
        current_x = self.player.xcor()
        self.player.setx(current_x - self.PLAYER_SPEED)

    def move_right(self) -> None:
        """Here the function receive the x coordinate & and then we add 20 from it."""
        self.player.penup()
        current_x = self.player.xcor()
        self.player.setx(current_x + self.PLAYER_SPEED)
