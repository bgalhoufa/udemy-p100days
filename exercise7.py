#!/usr/bin/env python3

print('Welcome to the Love Calculator!')
name1 = input('What is your name? \n')
name2 = input('What is their name? \n')

my_name1_count = len(name1)
my_name2_count = len(name2)
n = 0
z = 0
y = 0
x = 0

result_t1 = 0
result_t2 = 0
result_l1 = 0
result_l2 = 0


while n < my_name1_count:
    if name1[n] == 'T' or name1[n] == 'R' or name1[n] == 'U' or name1[n] == 'E':
        result_t1 += 1
    n += 1
while x < my_name1_count:
    if name1[x] == 'L' or name1[x] == 'O' or name1[x] == 'V' or name1[x] == 'E':
        result_l1 += 1
    x += 1

while y < my_name2_count:
    if name2[y] == 'T' or name2[y] == 'R' or name2[y] == 'U' or name2[y] == 'E':
        result_t2 += 1
    y += 1
while z < my_name2_count:
    if name2[z] == 'L' or name2[z] == 'O' or name2[z] == 'V' or name2[z] == 'E':
        result_l2+= 1
    z += 1


#print(my_name1_count)
print(f'The TRUE result for first name is {result_t1}')
print(f'The TRUE result for second name is {result_t2}')
print(f'The LOVE result for first name is {result_l1}')
print(f'The LOVE result for second name is {result_l2}')

my_sum_1 = int(f'{result_t1}{result_l1}')
my_sum_2 = int(f'{result_t2}{result_l2}')
my_sum_t = my_sum_1 + my_sum_2

print(my_sum_1)
print(my_sum_2)

if my_sum_t < 10 or my_sum_t > 90:
    print(f'Your score is {my_sum_t}, so you\'re like soda and coca cola')
if my_sum_t > 40 and my_sum_t < 50:
    print(f'Your score is {my_sum_t}, so you\'re alright together')
else:
    print(f'Your score is {my_sum_t}')


