#/usr/bin/env python3

print('Welcome to the tip calculator.')
my_bill = float(input('What was the total bill? '))
my_split = int(input('How many people to split the bill? '))
my_prctg = int(input('What percentage tip would you like to give? 10, 12, or 15? '))

total = round(my_bill + (my_prctg / my_bill) * 100)

p_total = round(total / my_split)

print(f' Total bill is {total} euros')
print(f' Each person has to pay {p_total} euros')
