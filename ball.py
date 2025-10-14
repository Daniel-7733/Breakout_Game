from turtle import Turtle


class Ball:
    def __init__(self) -> None:
        self.ball = Turtle()
        self.BALL_COLOR: str = "#f0f255"

        self.draw_ball()
        self.ball.speed(20)
        # self.ball_reset()

    def draw_ball(self) -> None:
        """Here I use turtle itself to make the circle"""

        self.ball.shape("circle")
        self.ball.color(self.BALL_COLOR)
        self.ball.penup()
        self.ball_reset()

    def ball_reset(self):
        """Resets the ball position"""
        self.ball.goto(x=0, y=-280)  # The original position

    def constant_movement(self) -> None:
        new_x = self.ball.xcor() + 3
        new_y = self.ball.ycor() + 3
        self.ball.goto(new_x, new_y)

        # call this function again after 20ms
        self.ball.getscreen().ontimer(self.constant_movement, 20)

