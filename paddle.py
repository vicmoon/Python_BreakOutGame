from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        #self.goto(position)


        #needs to follow the mouse 