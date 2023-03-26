#/usr/bin/env python3

from replit import clear
import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

my_word = random.choice(word_list)

display = []

for letter in my_word:
    display.append('_')
print('The word is:')
print('\n')
print(' '.join(display))
print('\n')
print('-' * 40)

my_tries = 6
gameover = False

while not gameover:
    my_guess = input('Please insert a letter to check if is in the word.\n').lower()
    clear()
    for position in range(len(my_word)):
        if my_word[position] == my_guess:
            display[position] = my_guess
    print(' '.join(display))

    if '_' not in display:
        print('YOU WON THE GAME')
        gameover = True
    
    if my_guess not in my_word:
        my_tries -= 1
        print('\n\n')
        print(f'Wrong letter {my_guess}, you have {my_tries} tries remaining')
        print(stages[my_tries])
        if my_tries > 0:
            continue
        else:
            gameover = True
            print('GAMEOVER')


