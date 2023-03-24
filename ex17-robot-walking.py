#/usr/bin/env python3

'''
This was an exercise from a 3rd party platform that is executed on browser:

hurdle 1,2,3,4

https://reeborg.ca/reeborg.html

'''


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while wall_on_right():
        if wall_in_front():
            break
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

