from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('turtle')


list_color = ['red', 'black', 'yellow', 'blue', 'brown', 'green']
list_side = ['right', 'left']
list_angle = [0, 90, 180, 270]

timmy.pensize(10)
timmy.speed(10)
x = True

while x:
    timmy.color(random.choice(list_color))
    timmy.forward(50)
    timmy.setheading(random.choice(list_angle))


screen = Screen()
screen.exitonclick()