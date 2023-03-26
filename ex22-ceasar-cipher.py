#!/usr/bin/env python3

from ex22logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

my_choice = 'yes'

def encryption(method):
    my_word = ''
    global my_choice
    for letter in text:
        if letter in alphabet:
            my_index = alphabet.index(letter)
            if method == 'decode':
                my_word = my_word + alphabet[my_index - shift]
            else:
                my_word = my_word + alphabet[my_index + shift]
        else:
            my_index = text.index(letter)
            my_word = my_word + text[my_index]
    print(f'The {method} word is {my_word}\n')
    print('-' * 80)
    print('-' * 80)
    print('\n')
    my_choice = input('Type \'yes\' .if you want to go again. Otherwise type \'no\'\n')


while my_choice == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        print('Please insert a value between 1 and 26')
        shift = int(input("Type the shift number:\n"))

    print('-' * 80)
    print('-' * 80)
    print('\n')
    encryption(direction)
    print('Goodbye')

