from turtle import Turtle
import turtle


class Paddle:
    def __init__(self) -> None:
        self.half_paddle: int | None = None
        self.screen = turtle.Screen()
        self.paddle: Turtle = Turtle()
        self.paddle_color: str = "#eef074"
        self.paddle.speed(100)
        self.paddle_shape()
        self.step: int = 100 # Speed of the paddle

        self.paddle.screen.onkey(self.move_left, "Left")
        self.paddle.screen.onkey(self.move_right, "Right")
        self.paddle.screen.listen()


    def paddle_shape(self) -> None:
        """Here I use turtle itself to make the rectangle"""
        self.paddle.shape("square")
        self.paddle.color(self.paddle_color)
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.penup()
        self.paddle.setpos(0, -300)
        self.half_paddle: int = 5 * 10


    def clamp_x(self, x: float) -> float :
        """
        This function make a boundaries in X-axis (-x, x) and won't let paddle go beyond certain number.
        :param x: float number on the X-axis
        :return: A valid float number on X-axis
        """

        half_width: float = self.screen.window_width() / 2
        left: float = -half_width + self.half_paddle
        right: float = half_width - self.half_paddle
        return max(min(x, right), left)


    def move_left(self) -> None:
        """When the left arrow-button is clicked, function will push the paddle to the left."""
        new_x: float = self.paddle.xcor() - self.step
        new_x: float = self.clamp_x(new_x)
        self.paddle.setx(new_x)


    def move_right(self) -> None:
        """When the right arrow-button is clicked, function will push the paddle to the right."""
        new_x: float = self.paddle.xcor() + self.step
        new_x: float = self.clamp_x(new_x)
        self.paddle.setx(new_x)
