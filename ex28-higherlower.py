#/usr/bin/env python3

from ex28art import logo, vs
from ex28gamedata import data
import random

print(logo)

win = False
my_score = 0

def first_choice():
    global my_result1
    my_random1 = random.randint(0, 49)
    my_name1 = data[my_random1]['name']
    my_desc1 = data[my_random1]['description']
    my_country1 = data[my_random1]['country']
    my_result1 = data[my_random1]['follower_count']
    print(f'Compare A: {my_name1}, a {my_desc1}, from {my_country1}, {my_result1}')

def second_choice():
    global my_result2
    my_random2 = random.randint(0, 49)
    my_name2 = data[my_random2]['name']
    my_desc2 = data[my_random2]['description']
    my_country2 = data[my_random2]['country']
    my_result2 = data[my_random2]['follower_count']
    print(f'Compare B: {my_name2}, a {my_desc2}, from {my_country2}, {my_result2}')

def my_game():
    global win
    if my_choice == 'A' and my_result1 > my_result2:
        print('Escolha 1')
        win = True
    elif my_choice == 'A' and my_result1 < my_result2:
        print(f'You Lost with A result {my_result1} against {my_result2}')
        win = False
    elif my_choice == 'B' and my_result1 > my_result2:
        print(f'You Lost with A result {my_result1} against {my_result2}')
        win = False
    elif my_choice == 'B' and my_result1 < my_result2:
        print('Escolha 4')
        win = True

first_choice()
print(vs)
second_choice()
my_choice = input('Who has more followers? Type \'A\' or \'B\': ')
my_game()

if win == True:
    my_score +=1
    print(f'You\'re right! Current score {my_score}')

while win == True:
    second_choice()
    my_choice = input('Who has more followers? Type \'A\' or \'B\': ')
    my_game()
    if win == False:
        break
    else:
        my_score +=1
        print(f'You\'re right! Current score {my_score}')
print(f'Final score is {my_score}')
