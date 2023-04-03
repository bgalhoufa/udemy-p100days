import random
import turtle as t

timmy = t.Turtle()
timmy.shape('turtle')
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

list_side = ['right', 'left']
list_angle = [0, 90, 180, 270]

timmy.pensize(10)
timmy.speed(10)
x = True

while x:
    my_color = random_color()
    timmy.color(my_color)
    timmy.forward(50)
    timmy.setheading(random.choice(list_angle))



screen = t.Screen()
screen.exitonclick()