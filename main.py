#Breakout game 
from turtle import Screen
from paddle import Paddle
from ball import Ball


""".....................................Movements and Collisions ...................."""


""".....................................UI SetUp...................................... """


screen =Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("BreakOut!")
screen.tracer(0)


ball = Ball()
# paddle = Paddle()


# game_on = True
# while game_on:
#     pass