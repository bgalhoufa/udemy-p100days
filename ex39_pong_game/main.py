from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
my_ball = Ball()
my_score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')
my_speed = 2
game_is_on = True

while game_is_on:
    time.sleep(my_ball.move_speed)
    screen.update()
    my_ball.move()
    if my_ball.ycor() > 280 or my_ball.ycor() < -280:
        my_ball.bounce_y()
    elif my_ball.distance(r_paddle) < 50 and my_ball.xcor() > 320 or my_ball.distance(l_paddle) < 50 and my_ball.xcor() < -320:
        my_ball.bounce_x()
    elif my_ball.xcor() > 400:
        my_score.increase_score_left()
        my_ball.reset()
    elif my_ball.xcor() < -400:
        my_score.increase_score_right()
        my_ball.reset()
    if my_score.score_right == 5 or my_score.score_left == 5:
        game_is_on = False
        my_score.game_over()

screen.exitonclick()