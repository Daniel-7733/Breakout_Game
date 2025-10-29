from turtle import Turtle, _Screen, TurtleScreen



class Ball:
    """
    Velocity-based ball movement (vx, vy) with:
    - wall bounces
    - paddle bounce (AABB)
    - brick collisions (AABB; removes one brick per tick)
    """
    def __init__(self, screen: _Screen) -> None:
        self.ball: Turtle = Turtle()
        self.ball.shape("circle")
        self.ball.color("#f0f255")
        self.ball.penup()
        self.ball.speed(0)  # fastest draw

        # font
        self.hub_font: str = "Pixeltype"

        # motion
        self.vx: float = 100/20 # v = x/t 100/20
        self.vy: float = 100/20 # v = x/t 100/20
        self.radius: int = 10  # default circle ~20px diameter

        # Score
        self.score: int = 0

        # This is for Score pen that write on top of the screen
        self.score_pen: Turtle = Turtle()
        self.score_pen.hideturtle()
        self.score_pen.color("#f0f255")
        self.score_pen.penup()
        self.score_pen.goto(-350, 350)

        self.update_score()
        self.screen = screen
        self.screen.tracer(0)


        self.is_game_over: bool = False

        # external refs
        self.paddle: Turtle | None = None
        # list of dicts from Brick.get_bricks(): [{"t": Turtle, "half_w": float, "half_h": float, "alive": bool}]
        self.bricks: list[dict[str, Turtle | float | bool]] = []

        self.ball_reset()


    # --- wiring from Game ---
    def set_paddle(self, paddle_turtle: Turtle) -> None:
        """
        Connect the paddle's Turtle instance to the ball.

        This allows the ball to access the paddle for collision detection
        or position tracking during gameplay.

        :param paddle_turtle: (Turtle) The Turtle object representing the paddle.
        :return: None
        """
        self.paddle = paddle_turtle


    def set_bricks(self, bricks: list[dict[str, Turtle | float | bool]]) -> None:
        """
        Assign the list of bricks that the ball can interact with.

        This method is typically called by the Game class to provide the
        ball with references to all active brick objects, enabling collision
        detection and brick removal logic.

        :param bricks: (list[BrickDict]): A list of brick dictionaries, where each
                dictionary contains the brick's Turtle instance, dimensions,
                and alive state.
                [{"t": Turtle, "half_w": float, "half_h": float, "alive": bool}]
        :return: None
        """
        self.bricks = bricks or []


    # --- control ---
    def ball_reset(self) -> None:
        """
        Reset the ball position
        :return: None
        """
        self.ball.goto(0, -280)
        self.vy = abs(self.vy) # ensure upward start after reset


    def start(self) -> None:
        """
        Paddle & ball start at the same time after the bricks completed. (20 Millisecond)
        :return: None
        """
        self.ball.getscreen().ontimer(self._tick, 20) # kick off the timer loop


    def _tick(self) -> None:
        """
        Update the ball's position and handle one frame of game logic.

        This method moves the ball based on its current velocity, checks for
        collisions with walls, the paddle, and bricks, and schedules the next
        frame update using `ontimer()`.

        It is called repeatedly (about every 20 ms) to animate the game loop.

        Returns:
            None
        """
        self.ball.goto(self.ball.xcor() + self.vx, self.ball.ycor() + self.vy) # update position

        # collisions
        self._handle_walls() # may clamp and invert
        if not self._handle_game_over():  # returns True if it reset / ended
            self.handle_paddle()
            self.handle_bricks()

        self.screen.update()
        # schedule next frame
        self.ball.getscreen().ontimer(self._tick, 17) # t: 16 or 17, will feel like 60fps


    # --- collisions ---
    def _handle_walls(self) -> None:
        """
        Detect and handle collisions between the ball and the screen boundaries.

        Reflects the ball's velocity when it hits the left, right, or top walls,
        and updates the internal bottom limit for detecting when the ball falls
        below the visible playfield.

        Returns:
            None
        """
        screen: TurtleScreen = self.ball.getscreen()
        half_w: float = screen.window_width() / 2
        half_h: float = screen.window_height() / 2

        left: float = -half_w + self.radius
        right: float =  half_w - self.radius
        bottom: float = -half_h + self.radius
        top: float =  half_h - self.radius

        x, y = self.ball.xcor(), self.ball.ycor()

        if x <= left or x >= right:
            self.vx *= -1
            self.ball.setx(max(min(x, right), left))

        if y >= top:
            self.vy *= -1
            self.ball.sety(top)

        # store for game-over check
        self._bottom_limit: float = bottom


    def _handle_game_over(self) -> bool:
        """
        Check if the ball has fallen below the visible playfield.

        If the ball passes below the bottom limit, this method triggers a
        game-over condition, prints a message, and resets the ball's position.

        Returns:
            bool: True if a game-over event occurred (the ball was reset),
                  False otherwise.
        """
        # fell below the visible playfield?
        if self.ball.ycor() <= self._bottom_limit:
            self.is_game_over = True
            self.paddle.enabled = False
            self.ball.goto(0, 0)
            self.ball.clear()
            self.ball.write("Game Over", align="center", font=(self.hub_font, 50, "bold"))
            # simple reset (you can call back to Game for score/lives)

            # stoping the ball speed & reset the ball position
            self.ball_reset()
            self.vx = 0
            self.vy = 0
            self.is_game_over = True
            return True
        return False


    def handle_paddle(self) -> None:
        """
        Detect and respond to collisions between the ball and the paddle.

        When the ball is moving downward and overlaps the paddle's area,
        it reflects vertically and applies a small horizontal adjustment
        ("english") based on where it hit the paddle to vary the bounce angle.

        Returns:
            None
        """
        if self.paddle is None or self.vy >= 0:
            return  # no paddle or ball is going up

        px, py = self.paddle.xcor(), self.paddle.ycor()
        sw, sl, *_ = self.paddle.shapesize()
        paddle_width: float = 20 * sl
        paddle_height: float = 20 * sw

        paddle_left: float = px - paddle_width / 2
        paddle_right: float = px + paddle_width / 2
        paddle_top: float = py + paddle_height / 2

        x, y = self.ball.xcor(), self.ball.ycor()
        ball_bottom: float = y - self.radius

        # horizontally over paddle & bottom is at or below the top edge
        if (paddle_left - self.radius) <= x <= (paddle_right + self.radius) and ball_bottom <= paddle_top and y > py:
            self.vy *= -1
            self.ball.sety(paddle_top + self.radius) # place the ball just above to avoid double-collision next frame

            hit_offset: float = (x - px) / (paddle_width / 2)  # -1..1
            self.vx += hit_offset * 0.8  # tweak to taste
            # cap vx a bit so it doesn't explode
            self.vx = max(min(self.vx, 8), -8)


    def handle_bricks(self) -> None:
        """
        Detect and handle collisions between the ball and bricks.

        Checks all active (alive) bricks for overlap with the ball and
        reflects the ball's velocity based on the side of impact.
        When a brick is hit, it becomes hidden and marked as inactive.

        Only one brick collision is processed per frame to prevent
        multiple hits at once.

        Returns:
            None
        """
        if not self.bricks:
            return

        x, y = self.ball.xcor(), self.ball.ycor()

        for b in self.bricks:
            if not b["alive"]:
                continue

            bt: Turtle = b["t"]
            bx, by = bt.xcor(), bt.ycor()

            # AABB vs circle-ish overlap
            if abs(x - bx) <= (b["half_w"] + self.radius) and abs(y - by) <= (b["half_h"] + self.radius):
                # compute overlap in each axis to decide reflection axis
                overlap_x: float = (b["half_w"] + self.radius) - abs(x - bx)
                overlap_y: float = (b["half_h"] + self.radius) - abs(y - by)

                if overlap_y < overlap_x:
                    self.vy *= -1  # hit top/bottom face
                else:
                    self.vx *= -1  # hit left/right face

                self.add_score()

                bt.hideturtle() # remove brick
                b["alive"]: bool = False
                # slight nudge out to avoid re-hitting same brick next frame
                if overlap_y < overlap_x:
                    self.ball.sety(by + (b["half_h"] + self.radius) * (1 if y >= by else -1))
                else:
                    self.ball.setx(bx + (b["half_w"] + self.radius) * (1 if x >= bx else -1))
                break  # only one brick per frame


    def update_score(self) -> None:
        """
        This function will display the score and updated score on screen

        :return: None
        """
        self.score_pen.clear()
        self.score_pen.write(f"Score: {self.score}", align="left", font=(self.hub_font, 30, "bold"))


    def add_score(self, points: int = 1) -> None:
        """
        This function will update the score by adding point to it. (If it uses in function like _handle_bricks()
         that detect the collision, then it will add points to score.)

        :param points: (Integer) It can be any number but by default it is 1
        :return: None
        """
        self.score += int(points)
        self.update_score()
