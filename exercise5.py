#!/usr/bin/env python3

my_year = int(input('Please type the year to check. '))

if my_year % 4 == 0: 
    if my_year % 100 == 0 and my_year % 400 == 0:
        print(f'The year {my_year} is leap')
    else:
        print('The year is not leap')
else:
    print('The year is not leap')
