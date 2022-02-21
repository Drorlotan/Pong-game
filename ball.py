from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(10)
        self.setheading(randint(-40,40))

    def move(self):
        self.forward(10)

    def hit(self):
        heading = self.heading()
        self.setheading(-heading)

    def hit_pads(self, pad, segment):
        if pad == 1:
            self.setheading(120 + segment*30)
        elif pad == 0:
            self.setheading(60 - segment*30)

    def middle(self):
        self.setx(0)
        self.sety(0)
        self.setheading(randint(-40, 40))

