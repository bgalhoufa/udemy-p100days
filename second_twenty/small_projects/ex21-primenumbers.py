#!/usr/bin/env python3

def prime_checker(number):
    is_prime = True
    if number <= 100:
        for i in range(2,number-1):
            if number % i == 0:
                is_prime = False
        if is_prime:
            print('It\'s a prime number')
        else:
            print('It\'s not a prime number')
    else:
        print('Please insert a number between 1 and 100')


n = int(input("Check this number: "))
prime_checker(number=n)
