from turtle import Screen, _Screen
from paddle import Paddle
from ball import Ball
from brick import Brick




class Game:
    """
    Main controller class for the Breakout game.

    This class sets up the game window, initializes all core objects
    (paddle, ball, and brick grid), and manages user input bindings.

    Responsibilities:
    - Configure the main window and visual theme.
    - Instantiate and connect the Paddle, Ball, and Brick systems.
    - Wire input controls for player movement.
    - Start the main game loop when requested.
    """

    def __init__(self) -> None:
        self.screen: _Screen = Screen()
        self.screen.title("Breakout (Turtle)")
        # fixed window size; ball uses dynamic window_width/height for bounds
        self.screen.setup(width=900, height=900)
        self.screen.bgcolor("#111218")

        # Create game objects
        self.paddle: Paddle = Paddle()
        self.ball: Ball = Ball(screen=self.screen, paddle_turtle=self.paddle.paddle)
        self.brick: Brick = Brick()

        self.is_running: bool = True

        # Wire references
        self.total_lives: int = self.brick.brick_length
        self.ball.total_bricks(count=self.total_lives)
        self.ball.set_bricks(self.brick.get_bricks())

        # ---------------------- Input ----------------------
        # right and left arrow in keyboard
        self.screen.listen()
        self.screen.onkeypress(self.paddle.move_left, "Left")
        self.screen.onkeypress(self.paddle.move_right, "Right")
        # WASD:
        self.screen.onkeypress(self.paddle.move_left, "a")
        self.screen.onkeypress(self.paddle.move_right, "d")

        self._tick()


    def _tick(self) -> None:
        """
        This function force the main game loop called repeatedly via ontimer

        :return: None
        """
        if not self.ball.is_game_over: # normal game update
            self.ball.handle_bricks()
            self.ball.handle_paddle()
        else: # Game over logic: disable paddle once
            self.paddle.enabled = False
            self.paddle.reset_position()
        self.screen.update()
        self.screen.ontimer(self._tick, 16)


    def start(self) -> None:
        """
        Start the Breakout game.

        Launches the ball movement and enters the Turtle event loop.
        This function blocks further execution until the window is closed.

        Typical usage:
            >>> game = Game()
            >>> game.start()

        :return: None
        """
        self.ball.start()
        self.screen.mainloop()
