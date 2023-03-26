#/usr/bin/env python3

from random import randint

my_luck = randint(0,1)

my_guess = int(input('Please give a guess, 0 for head or 1 for tail \n'))

if my_guess == 0 and my_luck == 0:
    print('You\'re guess was right you won with head')
if my_guess == 1 and my_luck == 1:
    print('You\'re guess was right you won with tail')

if my_guess == 0 and my_luck == 1:
    print('You\'re guess was wrong you loose with head againt tail')
if my_guess == 1 and my_luck == 0:
    print('You\'re guess was wrong you loose with tail against head')

