#/usr/bin/env python3

from ex26art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_cards = []
pc_cards = []

def my_calc(card1,card2):
    return card1 + card2

def play_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    my_cards = []
    pc_cards = []
    for _ in range (2):
        my_cards.append(int(random.choice(cards)))
        cards.remove(my_cards[-1])
        pc_cards.append(int(random.choice(cards)))
        cards.remove(pc_cards[-1])

    my_result = my_calc(my_cards[0], my_cards[1])
    pc_result = my_calc(pc_cards[0], pc_cards[1])
    print(f'Your cards: {my_cards}, current score: {my_result}')
    print(f'Computer\'s first card: {pc_cards[0]}')

    while pc_result < 17:
        pc_cards.append(int(random.choice(cards)))
        pc_result = pc_result + pc_cards[-1]

    next_play = input('Type \'y\' to get another card, type \'n\' to pass: ')

    while next_play == 'y':
        my_cards.append(int(random.choice(cards)))
        my_result = my_result + my_cards[-1]
        print(f'Your cards: {my_cards}, current score: {my_result}')
        if my_result > 21:
            break
        next_play = input('Type \'y\' to get another card, type \'n\' to pass: ')
    
    if my_result > pc_result and my_result <= 21:
        print('YOU WON THE GAME')
    elif my_result == pc_result:
        print('IT\'S A DRAW')
    elif pc_result > 21 and my_result < 21:
        print('YOU WON BECAUSE PC RESULT IS GREATER THAN 21')
    elif pc_result > my_result:
        print('PC WON THE GAME')
    print('\n\n\n\n')
    print(f'Your cards: {my_cards}, current score: {my_result}')
    print(f'PC cards: {pc_cards}, current score: {pc_result}')


while input('Do you want to play a game of Backjack? Type \'y\' or \'n\': ') == 'y':
    play_game()
 
