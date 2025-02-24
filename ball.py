from turtle import Turtle 

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.y_move = 3
        self.x_move = 3
        

    def change_position(self):
        random_x = self.xcor() + self.x_move
        random_y = self.ycor() + self.y_move
        self.goto(random_x, random_y)


    #bounce y 
    def bounce_y(self):
        self.y_move *= -1 

    #bounce x 
    def bounce_x(self):
        self.x_move *= -1
    

    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 1
        self.bounce_y()


