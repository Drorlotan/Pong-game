from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = [0,0]
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,200)
        self.write(arg=f"score: {self.score[0]}  {self.score[1]}", align="center")

    def add_score_left(self):
        self.clear()
        self.score[0] += 1
        self.write(arg=f"score: {self.score}", align=("center"))

    def add_score_right(self):
        self.clear()
        self.score[1] += 1
        self.write(arg=f"score: {self.score}", align=("center"))


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER")