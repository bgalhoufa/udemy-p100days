import turtle
from turtle import Turtle, Screen
from ex37_turtle_init import NewTurtle
import random

#tim = NewTurtle('tim', 'red')

screen = Screen()
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
username =['tim', 'bruno', 'john', 'Vasco', 'Xavier', 'Walt']
user_bet = screen.textinput('Make your bet', 'Which turtle wins the race? Enter a colo: ')
posy = -60
is_race_on = False

for i in range(6):
    username[i] = Turtle(shape='turtle')
    username[i].color(colors[i])
    username[i].penup()
    username[i].goto(-230, posy)
    posy += 30
    #username[i].forward(460)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in username:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f'You\'ve won! The {winner} turtle is the winner ')
                is_race_on = False
                break
            else:
                print(f'You\'ve lost! The {winner} turtle is the winner ')
                is_race_on = False
        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)


screen.exitonclick()