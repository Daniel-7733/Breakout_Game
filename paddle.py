from turtle import Turtle, TurtleScreen


class Paddle:
    """
    Simple left/right paddle with boundary clamps, using a stretched square.
    """
    def __init__(self) -> None:
        self.paddle: Turtle = Turtle()
        self.paddle.shape("square")
        self.paddle.color("#6bc2ff")
        self.paddle.penup()
        self.paddle.shapesize(stretch_wid=1.0, stretch_len=6.0) # height ~20px * 1, width ~20px * 6 => ~120px wide
        self.paddle.speed(0)
        self.paddle.goto(0, -320)

        self.step: int = 30  # movement config: pixels per keypress (Speed)
        self.enabled: bool = True # control flag


    def reset_position(self) -> None:
        """
        Reposition the paddle and turn off and in addition, will change the value of enabled to false

        :return: None
        """
        self.paddle.goto(0, -320)
        self.enabled = False

    def move_left(self) -> None:
        """
        Move to left when a key press by user
        :return: None
        """
        screen: TurtleScreen = self.paddle.getscreen()
        half_w: float = screen.window_width() / 2
        width_px: float = 20 * self.paddle.shapesize()[1]
        left_limit: float = -half_w + width_px / 2
        new_x: float = max(self.paddle.xcor() - self.step, left_limit)
        self.paddle.setx(new_x)

    def move_right(self) -> None:
        """
        Move to right when a key press by user
        :return: None
        """
        screen: TurtleScreen = self.paddle.getscreen()
        half_w: float = screen.window_width() / 2
        width_px: float = 20 * self.paddle.shapesize()[1]
        right_limit: float = half_w - width_px / 2
        new_x: float = min(self.paddle.xcor() + self.step, right_limit)
        self.paddle.setx(new_x)

    def paddle_position(self) -> tuple[float, float, float, float]:
        """
        Reveal position of paddle.
        :return: tuple(paddle x, paddle y, width px, height px)
        """
        sw, sl, *_ = self.paddle.shapesize()
        width_px: float = 20 * sl
        height_px: float = 20 * sw
        return self.paddle.xcor(), self.paddle.ycor(), width_px, height_px
