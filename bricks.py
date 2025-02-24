from turtle import Turtle

#how to generate bricks? 
class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2.5)
        self.color("green")
        self.fillcolor("blue")
        self.penup()
        self.is_visible = True
      

#how to make them disappear when colliding with the ball? 

    def hide(self):
        if self.is_visible:
            self.hideturtle()
            self.is_visible = False
            return True
        return False
    
    def check_brick_collision(brick, bricks):
        for brick in bricks:
            if brick.is_visible:
                brick_left = brick.xcor() - 25 
                brick_right = brick.xcor() + 25 
                brick_top = brick.ycor() + 10 
                brick_bottom = brick.ycor() -10 

                ball_x = ball.xcor()
                
