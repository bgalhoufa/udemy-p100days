#/usr/bin/env python

'''
S - 15
M - 20
L - 25

Pep S - 2
Pep M/L - 3

Cheese - 1
'''

print('Welcome to Python Pizza Deliveries!')
size = input('What Size of pizza do you want? (S or M or L) \n')
add_pep = input('Do you want pepperoni? (Y or N)\n')
extra_c = input('Do you want extra cheese? (Y or N)\n')

p_small = 15
p_medium = 20
p_large = 25

pep_small = 2
pep_morl = 3

cheese = 1


if size == 'S':
    if add_pep == 'Y' and extra_c == 'Y':
        total = p_small + pep_small + cheese
        print(f'Your total price is {total}')
    elif add_pep == 'Y' and extra_c == 'N':
        total = p_small + pep_small
        print(f'Your total price is {total}')
    elif add_pep == 'N' and extra_c == 'Y':
        total = p_small + pep_cheese
        print(f'Your total price is {total}')
    else:
        total = p_small
        print(f'Your total price is {total}')
if size == 'M':
    if add_pep == 'Y' and extra_c == 'Y':
        total = p_medium + pep_morl + cheese
        print(f'Your total price is {total}')
    elif add_pep == 'Y' and extra_c == 'N':
        total = p_medium + pep_morl 
        print(f'Your total price is {total}')
    elif add_pep == 'N' and extra_c == 'Y':
        total = p_medium + pep_cheese
        print(f'Your total price is {total}')
    else:
        total = p_medium
        print(f'Your total price is {total}')
if size == 'L':
    if add_pep == 'Y' and extra_c == 'Y':
        total = p_large + pep_morl + cheese
        print(f'Your total price is {total}')
    elif add_pep == 'Y' and extra_c == 'N':
        total = p_large + pep_morl
        print(f'Your total price is {total}')
    elif add_pep == 'N' and extra_c == 'Y':
        total = p_large + pep_cheese
        print(f'Your total price is {total}')
    else:
        total = p_large
        print(f'Your total price is {total}')



#print(type(size))
