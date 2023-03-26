#!/usr/bin/env python3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
print('-' * 80)
print('-' * 80)
print('\n')

def encrypt():
    my_word = ''
    for letter in text:
        my_index = alphabet.index(letter)
        my_word = my_word + alphabet[my_index + shift]
    print(my_word)

encrypt()

