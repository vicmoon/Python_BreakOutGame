#Breakout game 
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard




""".....................................UI SetUp...................................... """


screen =Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("BreakOut!")
screen.tracer(0)


ball = Ball()
paddle = Paddle()
scoreboard = Scoreboard()



""".....................................Movements and Collisions ...................."""

# Variable to store mouse position
mouse_x, mouse_y = 0, 0

def get_mouse_coordinates(x, y):
    global mouse_x, mouse_y
    mouse_x, mouse_y = x, y

def move_paddle():
    paddle.goto(mouse_x, paddle.ycor())
    screen.update()
    screen.ontimer(move_paddle, 10)


screen.onscreenclick(get_mouse_coordinates)
screen.ontimer(move_paddle, 10)



screen.listen()

screen.update()


# Keep the screen open
screen.mainloop()