from turtle import Turtle


class Brick(Turtle):
    def __init__(self, brick_width, brick_height):
        super().__init__()
        self.shape("square")
        width_stretch = brick_width / 20
        height_stretch = brick_height / 20
        self.shapesize(stretch_wid=height_stretch,stretch_len=width_stretch)
        self.color("green")
        self.fillcolor("blue")
        self.penup()
        self.is_visible = True
      


    def hide(self):
        if self.is_visible:
            self.hideturtle()
            self.is_visible = False
            return True
        return False
    
