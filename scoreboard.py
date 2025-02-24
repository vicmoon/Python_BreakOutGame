from turtle import Turtle
ALIGNMENT= "center"
FONT= ("courier", 30, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 0)
        self.write(self.score, f"Score: {self.score}", align=ALIGNMENT, font=FONT)
       


    def add_point(self):
        self.score += 1
        self.update_scoreboard()
    