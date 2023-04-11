#/usr/bin/env python3

from ex23logo import logo

print(logo)

print ('Welcome to the secret auction program.')

my_dict = {}
my_list = []
highest_bid = 0

def my_auction():
    add_new = 'yes'
    while add_new == 'yes':
        my_name = input('Please insert your name\n')
        my_bid = input('Please insert your bid\n')
        my_dict[my_name] = my_bid
        add_new = input('Do you want do add more players? yes/no \n')

def my_score():
    highest_bid = 0
    winner = ''
    for bidder in my_dict:
        value = int(my_dict[bidder])
        if value > highest_bid:
            highest_bid = value
            winner = bidder
    print(f'The winner is {winner}')


my_auction()
my_score()

