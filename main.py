from turtle import Screen, Turtle
import score
import pads
import ball
import time

screen = Screen()
screen.setup(width=700, height=500)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
screen.listen()



# make the doted line in the middle
doted_line = Turtle()
doted_line.color("white")
doted_line.penup()
doted_line.goto(0, -300)
doted_line.pendown()
doted_line.setheading(90)
for i in range(100):
    doted_line.forward(20)
    doted_line.penup()
    doted_line.forward(20)
    doted_line.pendown()

left_pad = pads.Pad()
left_pad.left_pad()
right_pad = pads.Pad()
right_pad.right_pad()
all_pads = [left_pad, right_pad]
score = score.Score()
ball = ball.Ball()

screen.onkey(right_pad.up, "Up")
screen.onkey(right_pad.down, "Down")
screen.onkey(left_pad.up, "w")
screen.onkey(left_pad.down, "s")

game_speed = 0
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.015-game_speed)
    ball.move()
    for pad in all_pads:
        pad_num = all_pads.index(pad)
        for segment in pad.segments:
            seg_num = pad.segments.index(segment)
            if ball.distance(segment) < 20:
                ball.hit_pads(pad=pad_num, segment=seg_num)
    if ball.ycor() > 240 or ball.ycor() < -240:
        ball.hit()
    if ball.xcor() > 340:
        score.add_score_left()
        ball.middle()
    if ball.xcor() < -340:
        score.add_score_right()
        ball.middle()
    if game_speed < 0.01:
        game_speed = 0.001*(sum(score.score))



screen.exitonclick()




