import random
import turtle as t

timmy = t.Turtle()
timmy.shape('turtle')
t.colormode(255)
timmy.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def draw_spirograph(gap):
    for _ in range(int(360/gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)

draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()