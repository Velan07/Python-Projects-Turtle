from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.screensize(600, 400, "black")
screen.listen()


r_paddle = Paddle((330, 0))
l_paddle = Paddle((-335, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 300) or (ball.distance(l_paddle) < 50 and ball.xcor() < -300):
        ball.bounce_x()

    if ball.distance(r_paddle) > 50 and ball.xcor() > 340:
        ball.reset_pos()
        scoreboard.l_point()
    elif ball.distance(l_paddle) > 50 and ball.xcor() < -340:
        ball.reset_pos()
        scoreboard.r_point()


screen.exitonclick()