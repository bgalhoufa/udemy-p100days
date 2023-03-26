#/usr/bin/env python3

from random import randint, choice

ppl_num = input('Please insert the name of persons to make the draw \n')

ppl_list = ppl_num.split(',')

my_choosen = choice(ppl_list)

#my_list_size = len(ppl_list) - 1

#ppl_draw = randint(0,my_list_size)

#my_choosen = ppl_list[ppl_draw]



print(f'Who will pay the bill is {my_choosen}')
