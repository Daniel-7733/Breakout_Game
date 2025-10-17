from turtle import Turtle


class Ball:
    def __init__(self) -> None:
        self.ball = Turtle()
        self.BALL_COLOR: str = "#f0f255"

        # velocity (pixels per tick)
        self.vx = 3.0
        self.vy = 3.0
        self.radius = 10  # default turtle "circle" is about 20x20 px

        self.draw_ball()


    def draw_ball(self) -> None:
        """Making the ball"""
        self.ball.shape("circle")
        self.ball.color(self.BALL_COLOR)
        self.ball.penup()
        self.ball_reset()


    def ball_reset(self):
        """Reset the ball position to the original position"""
        self.ball.goto(x=0, y=-280)


    def constant_movement(self) -> None:
        """Force the ball to constantly move"""
        # update position using velocity
        new_x = self.ball.xcor() + self.vx
        new_y = self.ball.ycor() + self.vy
        self.ball.goto(new_x, new_y)

        self.movement_law()

        self.ball.getscreen().ontimer(self.constant_movement, 20) # schedule next tick


    def movement_law(self):
        """Rules: Balls can't pass the boarder, and it should be inside the windows not outside"""
        screen = self.ball.getscreen()
        # get current window dimensions
        half_w: float = screen.window_width() / 2
        half_h: float = screen.window_height() / 2

        # playable bounds (keep the ball fully inside)
        left: float = -half_w + self.radius
        right: float =  half_w - self.radius
        bottom: float = -half_h + self.radius
        top: float =  half_h - self.radius

        x, y = self.ball.xcor(), self.ball.ycor()

        # bounce horizontally
        if x <= left or x >= right:
            self.vx *= -1
            # clamp to avoid sticking outside
            self.ball.setx(max(min(x, right), left))

        # bounce vertically
        if y <= bottom or y >= top:
            self.vy *= -1
            self.ball.sety(max(min(y, top), bottom))

        if y <= bottom:
            print("Game Over")
