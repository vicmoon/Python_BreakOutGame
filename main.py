#Breakout game 
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


""".....................................Movements and Collisions ...................."""


""".....................................UI SetUp...................................... """


screen =Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("BreakOut!")
screen.tracer(0)


ball = Ball()
paddle = Paddle()
scoreboard = Scoreboard()


# game_on = True
# while game_on:
#     pass

screen.listen()


screen.update()


# Keep the screen open
screen.mainloop()