#!/usr/bin/env python3

'''
This was an exercise from a 3rd party platform that is executed on browser:

MAZE

https://reeborg.ca/reeborg.html

'''


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
    while front_is_clear():
            move()
    else:
        while wall_on_right() and not at_goal():
            while front_is_clear():
                move()
            while wall_in_front() and wall_on_right():
                turn_left()
        while wall_in_front() and not wall_on_right() and not at_goal():
            turn_right()
            move()
        if is_facing_north() and front_is_clear():
            move()
