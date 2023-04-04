from turtle import Turtle, Screen

'''
W - forward
S - Backwards
A - Counterclockwise
D - clockwise
'''

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def move_clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(move_right, 'a')
screen.onkey(move_left, 'd')
screen.onkey(move_clear, 'c')


screen.exitonclick()