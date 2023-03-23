#/usr/bin/env python3

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

from random import randint

pc_number = randint(0,2)

my_choice = int(input('Please insert your choice 0 for paper, 1 for scissors, 2 for stone \n'))

if my_choice == 0 and pc_number == 0:
    print('We\'ve a tie both choose paper')
    print(paper)
if my_choice == 0 and pc_number == 1:
    print('You loose with paper against scissor')
    print(paper)
    print(scissors)
if my_choice == 0 and pc_number == 2:
    print('You won with paper against stone')
    print(paper)
    print(stone)

if my_choice == 1 and pc_number == 1:
    print('We\'ve a tie both choose scissor')
    print(scissors)
if my_choice == 1 and pc_number == 0:
    print('You won with scissor against paper')
    print(scissors)
    print(paper)
if my_choice == 1 and pc_number == 2:
    print('You loose with scissor against stone')
    print(scissors)
    print(stone)

if my_choice == 2 and pc_number == 2:
    print('We\'ve a tie both choose stone')
    print(stone)
if my_choice == 2 and pc_number == 1:
    print('You won with stone against scissor')
    print(stone)
    print(scissors)
if my_choice == 2 and pc_number == 0:
    print('You loose with stone against paper')
    print(stone)
    print(paper)





#print(number)
