import turtle
import random

turtle.colormode(255)
timmy = turtle.Turtle()
my_colors = [(207, 160, 82), (54, 89, 130), (145, 91, 40), (139, 27, 49), (222, 206, 109), (132, 176, 202)]
yposition = -300
timmy.hideturtle()
timmy.penup()
timmy.setx(-300)
timmy.sety(-300)

for _ in range(10):
    yposition = yposition+50
    timmy.penup()
    timmy.setx(-300)
    timmy.sety(yposition)
    for _ in range(10):
        timmy.penup()
        timmy.dot(20, random.choice(my_colors))
        timmy.forward(50)




screen = turtle.Screen()
screen.exitonclick()