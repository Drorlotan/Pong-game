from turtle import Turtle
UP = 90
DOWN = 270

class Pad(Turtle):

    def __init__(self):
        super().__init__()
        pad_segments = []
        for i in range(5):
            num = i
            i = Turtle("square")
            i.color("red")
            i.penup()
            i.right(90)
            i.forward(20*num)
            pad_segments.append(i)
        self.segments = pad_segments

    def left_pad(self):
        for segment in self.segments:
            segment.setheading(180)
            segment.forward(340)

    def right_pad(self):
        for segment in self.segments:
            segment.setheading(0)
            segment.forward(330)

    def up(self):
        if self.segments[0].ycor() < 320:
            for segment in self.segments:
                segment.setheading(UP)
                segment.forward(55)

    def down(self):
        if self.segments[-1].ycor() > -300:
            for segment in self.segments:
                segment.setheading(DOWN)
                segment.forward(55)
