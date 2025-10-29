from turtle import Turtle



BRICK_W: int = 100  # pixels
BRICK_H: int = 50   # pixels

class Brick:
    """
    Builds a grid of individual Turtle sprites for bricks.
    Each brick has its own turtle (easy to hide on hit) and cached half sizes for fast AABB checks.
    """
    def __init__(self) -> None:
        self.BRICK_COLOR: str = "#d66829"
        self.PEN_COLOR: str = "#221824"
        self.bricks: list[dict[str, Turtle | float | bool]] = []  # list of dicts: {"t": Turtle, "half_w": float, "half_h": float, "alive": bool}
        self._build_grid()
        self.brick_length = len(self.bricks)
        self.dead_count = sum(1 for brick in self.bricks if not brick["alive"])

    def _new_brick(self, cx: int, cy: int) -> dict[str, Turtle | float | bool]:
        """
        Create a single brick (Turtle object) positioned at the given center coordinates.

        Each brick:
        - Uses a square shape stretched to match the configured brick width and height.
        - Has its own Turtle instance for easy visibility toggling (e.g. on collision).
        - Stores precomputed half-width/height values for fast AABB collision checks.

        :param cx: X-coordinate of the brick's center (in pixels).
        :param cy: Y-coordinate of the brick's center (in pixels).
        :return: A dictionary representing the brick with:
                 {
                     "t": Turtle object for this brick,
                     "half_w": half of BRICK_W,
                     "half_h": half of BRICK_H,
                     "alive": True (brick starts visible and active)
                 }
        """

        t: Turtle = Turtle()
        t.hideturtle()
        t.shape("square")
        t.color(self.BRICK_COLOR)
        t.pencolor(self.PEN_COLOR)
        t.width(2)
        t.penup()
        t.shapesize(stretch_wid=BRICK_H / 20.0, stretch_len=BRICK_W / 20.0) # Base square is ~20x20 px; stretch to our desired brick size
        t.goto(cx, cy)
        t.showturtle()
        return {
            "t": t,
            "half_w": BRICK_W / 2.0,
            "half_h": BRICK_H / 2.0,
            "alive": True
        }

    def _build_grid(self) -> None:
        """
        Create a grid of bricks aligned in neat rows and columns.

        Grid layout:
        - X centers: -350 ... 350 (step 100) → fits 8 columns on a ~900px wide window.
        - Y centers: 150 ... 300 (step 50) → 4 rows by default.

        This method populates self.bricks with all brick dictionaries returned by `_new_brick()`.

        :return: None
        """
        for cy in range(150, 301, BRICK_H): # 150, 200, 250, 300
            for cx in range(-350, 351, BRICK_W): # -350, -250, ... , 350
                self.bricks.append(self._new_brick(cx, cy))

    def get_bricks(self) -> list[dict[str, Turtle | float | bool]]:
        """
        Return the list of all brick dictionaries currently managed by this Brick instance.

        Each element in the list is a dict containing:
        - "t": the Turtle object for drawing and visibility control,
        - "half_w": precomputed half-width of the brick (for collision checks),
        - "half_h": precomputed half-height of the brick,
        - "alive": boolean flag indicating if the brick is still visible/active.

        :return: List of brick dictionaries.
        """
        return self.bricks
