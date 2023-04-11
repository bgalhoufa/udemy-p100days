from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')

#for i in range(4):
#    timmy.forward(100)
#    timmy.right(90)

for _ in range(10):
    timmy.forward(10)
    timmy.up()
    timmy.forward(10)
    timmy.pendown()



screen = Screen()
screen.exitonclick()