from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.color("white")
        self.penup()
        self.goto(0, -250)


         

     

    



