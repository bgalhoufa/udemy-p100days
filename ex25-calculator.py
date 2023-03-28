#/usr/bin/env python3

from ex25art import logo

print(logo)

def add(n1,n2):
    return n1 + n2
def substract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

my_dict_op = {
        '+': add,
        '-': substract,
        '*': multiply,
        '/': divide
        }

def first_calc():
    my_first_n = float(input('What\'s the first number?: '))
    print('+\n-\n*\n/ ')
    my_operation = input('Pick an operation: ')
    my_second_n = float(input('What\'s the second number?: '))
    calc_function = my_dict_op[my_operation]
    answer1 = calc_function(my_first_n, my_second_n)
    print(f'{my_first_n} {my_operation} {my_second_n} = {answer1}')
    my_continue = input(f'Type \'y\' to continue calculating with {answer1}, or type \'n\' to exit: ')

    while my_continue == 'y':
        my_operation = input('Pick another operation: ')
        my_third_n = float(input('What\'s the next number?: '))
        calc_function = my_dict_op[my_operation]
        answer2 = calc_function(answer1, my_third_n)
        print(f'{answer1} {my_operation} {my_third_n} = {answer2}')
        answer1 = answer2
        my_continue = input(f'Type \'y\' to continue calculating with {answer1}, or type \'n\' to exit: ')
    return

first_calc()

