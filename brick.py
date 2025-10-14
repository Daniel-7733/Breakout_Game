from turtle import Turtle



class Brick:
    def __init__(self) -> None:
        self.br = Turtle()
        self.BRICK_COLOR: str = "#d66829"
        self.br.shape("turtle")
        self.br.speed(100)

        self.layer_all_bricks()

    def brick(self, x:int=0, y:int=0) -> None:
        self.br.up() # take the pen up to now draw the line when it changes the position
        self.br.setpos(x, y)
        self.br.down() # take the pen down to draw the shape.

        self.br.color(self.BRICK_COLOR)
        self.br.begin_fill()
        self.br.pencolor("#221824")
        self.br.width(5) # Making the lines between the bricks bigger

        for i in range(4):
            if i % 2 == 0:
                self.br.forward(100)
            else:
                self.br.forward(50)
            self.br.left(90)

        self.br.end_fill()

    def layer_all_bricks(self) -> None:
        for i in range(0, 300, 50):
            for j in range(-400, 400, 100):
                self.brick(j, i)