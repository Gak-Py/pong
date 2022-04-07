from turtle import Screen
from bar import Bar
from scoreboard import ScoreBoard
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("PONG")

screen.tracer(0)

ball = Ball()
score_board = ScoreBoard()

bar_l = Bar(-360, 40)
bar_r = Bar(350, 40)

screen.listen()
screen.onkey(bar_r.go_up, "[")
screen.onkey(bar_r.go_down, "]")
screen.onkey(bar_l.go_up, "q")
screen.onkey(bar_l.go_down, "a")

game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.xcor() >= 400:
        score_board.get_point("left")
        ball.ball_reset()

    if ball.xcor() <= -400:
        score_board.get_point("right")
        ball.ball_reset()

    if bar_l.distance(ball) < 30 and ball.xcor() <= -340 or bar_r.distance(ball) < 30 and ball.xcor() >= 310:
        ball.bounce_x()
    screen.update()

screen.exitonclick()


