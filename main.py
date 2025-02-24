#Breakout game 
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from bricks import Brick




""".....................................UI SetUp...................................... """


screen =Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("BreakOut!")
screen.tracer(0)


ball = Ball()
paddle = Paddle()





rows = 4   # Number of rows
cols = 10  # Number of columns
brick_width = 50  # Adjust based on Brick size
brick_height = 20  # Adjust based on Brick size
start_x = -225  # Adjust to center bricks on screen
start_y = 250   # Adjust to position at the top

#total width 
total_bricks_width = cols * brick_width

#starting point 
start_x = -total_bricks_width / 2 
start_y = 250 

bricks = []
for row in range(rows):
    for col in range(cols):
        brick = Brick()
        x_pos = start_x + (col * brick_width)  # Adjust X position
        y_pos = start_y - (row * brick_height)  # Adjust Y position
        brick.goto(x_pos, y_pos)  # Move brick to position
        bricks.append(brick) 





""".....................................Movements and Collisions ...................."""

# Variable to store mouse position
mouse_x = 0

def get_mouse_coordinates(x, y):
    global mouse_x
    mouse_x = x  # Update X position

def move_paddle():
    paddle.goto(mouse_x, paddle.ycor())  # Move paddle only in the X direction
    screen.update()
    screen.ontimer(move_paddle, 10)  # Keep updating paddle movement


def check_brick_collision(ball, bricks):
    for brick in bricks:
        if brick.is_visible:
            # Adjust these values based on your ball and brick sizes
            brick_left = brick.xcor() - 25  # Half of brick width
            brick_right = brick.xcor() + 25
            brick_top = brick.ycor() + 10   # Half of brick height
            brick_bottom = brick.ycor() - 10
            
            ball_x = ball.xcor()
            ball_y = ball.ycor()
            
            # Simple collision detection
            if (brick_left <= ball_x <= brick_right and 
                brick_bottom <= ball_y <= brick_top):
                ball.y_move *= -1  # Reverse ball's vertical direction
                brick.hide()   # Make the brick disappear
                return True    # Return True to indicate a collision
    return False



def move_ball():

    ball.change_position()  

    #ball boundaries 

    ball_x, ball_y = ball.xcor(), ball.ycor()
    paddle_x = paddle.xcor()
    

    #collision with the bricks 
    if check_brick_collision(ball, bricks):
        print("Collision with the bricks!")

    #collision with top wall 

    if ball_y >= 290:
        ball.bounce_y()

    #collision with side walls 

    if ball_x >=290 or ball_x <= -290:
        ball.bounce_x()

    #collision with paddle 

    if ball.distance(paddle) < 50 and ball_y < -250:
        offset = ball_x - paddle_x
        ball_x = offset * 0.1 
        ball.bounce_y()

    if ball_y <= -290:
        ball.reset_position()

    screen.update()
    screen.ontimer(move_ball, 20)  # Keep updating ball movement every 20ms




# Track mouse movements
screen.onscreenclick(get_mouse_coordinates)

# Start the movement loops
screen.ontimer(move_paddle, 10)  
screen.ontimer(move_ball, 20)  # Now the ball keeps moving

screen.listen()
screen.mainloop()