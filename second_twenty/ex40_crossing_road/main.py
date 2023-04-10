import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

my_game = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

my_turtle = Player()
my_car = CarManager()
my_score = Scoreboard()

screen.listen()
screen.onkey(my_turtle.go_up, 'Up')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    my_car.init_car()
    my_car.move_cars()
    my_score.update_scoreboard()

    for car in my_car.all_cars:
        if car.distance(my_turtle) < 20:
            my_score.game_over()
            game_is_on = False
        else:
            continue

    if my_turtle.ycor() == 300:
        my_turtle.go_to_start()
        my_car.increase_speed()
        my_score.increase_score()
    else:
        continue



screen.exitonclick()