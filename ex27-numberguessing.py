#/user/bin/env python3

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a number between 1 and 100')

my_number = range(101)

my_choice = random.choice(my_number)

my_difficulty = input('Choose a difficulty level. Type \'easy\' or \'hard\': ')

def my_func_diff(my_tries):
    won = False
    while my_tries > 0 and won != True:
        print(f'You have {my_tries} attempts remaining to guess the number.')
        my_guess = int(input('Make a guess\n'))
        if my_guess == my_choice:
            print(f'You won the game with number {my_guess}')
            won = True
        elif my_guess > my_choice:
            print('Too high')
            my_tries -= 1
        elif my_guess < my_choice:
            print('Too low')
            my_tries -= 1
    if won == False:
        print('You lost the game, please try again')

if my_difficulty == 'easy':
    my_func_diff(10)
if my_difficulty == 'hard':
    my_func_diff(5)
