from turtle import Turtle 

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.y_move = 10
        self.x_move = 10
        self.ball_speed = 10 


    def change_position(self):
        random_x = self.xcor() + self.x_move
        random_y = self.ycor() + self.y_move
        self.goto(random_x, random_y)


    #bounce y 
    def bounce_y(self):
        self.y_move *= -1 

    #bounce x 
    def bounce_x(self):
        self.x_move *= 0.9


