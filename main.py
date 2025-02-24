#Breakout game 
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from bricks import Brick
import time

def reset_game():
    """Reset the game state for a new round"""
    global bricks, ball
    
    # Clear existing bricks
    for brick in bricks:
        brick.hideturtle()
    bricks.clear()
    
    # Reset ball position
    ball.reset_position()

    score.clear()
    
    
    # Create new bricks
    for row in range(rows):
        for col in range(cols):
            brick = Brick(brick_width=brick_width, brick_height=brick_height)
            x_pos = start_x + (col * brick_width) + (brick_width / 2)  
            y_pos = start_y - (row * brick_height)
            brick.goto(x_pos, y_pos)
            bricks.append(brick)
    
    # Resume game
    screen.ontimer(move_ball, 20)


""".....................................UI SetUp...................................... """


screen =Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("BreakOut!")
screen.tracer(0)


ball = Ball()
paddle = Paddle()
score = Scoreboard()

screen_width = screen.window_width()  
screen_height = screen.window_height() 


rows = 5   # Number of rows
cols = 8  # Number of columns

available_width = screen_width
brick_width = available_width / cols
brick_height = 30

#starting point 
start_x = (-screen_width / 2 ) 
start_y = 250 

bricks = []
for row in range(rows):
    for col in range(cols):
        brick = Brick(brick_width=brick_width, brick_height=brick_height)

        x_pos = start_x + (col * brick_width) + (brick_width / 2)  
        y_pos = start_y - (row * brick_height)
        brick.goto(x_pos, y_pos)  # Move brick to position
        bricks.append(brick) 




""".....................................Movements and Collisions ...................."""

# Variable to store mouse position
mouse_x = 0
game_paused = False

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
    global game_paused

    if game_paused:
        return

    ball.change_position()  

    #ball boundaries 

    ball_x, ball_y = ball.xcor(), ball.ycor()
    paddle_x = paddle.xcor()
    

    #collision with the bricks 
    if check_brick_collision(ball, bricks):
        score.add_point()
        score.update_scoreboard()

    #collision with top wall 

    if ball_y >= 290:
        ball.bounce_y()

    #collision with bottom wall

    if ball_y <= -290:
        ball.game_over()
        game_paused = True
        
        #schedule sleep 
        screen.ontimer(lambda: restart_after_death(), 2000)
        return 
        

    #collision with side walls 

    if ball_x >=290 or ball_x <= -290:
        ball.bounce_x()

    #collision with paddle 

    if ball.distance(paddle) < 50 and ball_y < -230:
        offset = ball_x - paddle_x
        ball_x = offset * 0.3 
        ball.bounce_y()

    if ball_y <= -290:
        ball.reset_position()


    screen.update()
    screen.ontimer(move_ball, 20)  # Keep updating ball movement every 20ms

def restart_after_death():
    global game_paused
    game_paused = False
    reset_game()




# Track mouse movements
screen.onscreenclick(get_mouse_coordinates)

# Start the movement loops
screen.ontimer(move_paddle, 10)  
screen.ontimer(move_ball, 20)  # Now the ball keeps moving

screen.listen()
screen.mainloop()