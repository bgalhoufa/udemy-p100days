#/usr/bin/env python3

my_weight = float(input('What is your weight in kg?\n'))
my_height = float(input('What is your height in meters?\n'))

my_bmi = round(my_weight / my_height**2)

print(f'Your BMI value is {my_bmi}')

if my_bmi < 18.5:
    print('You\'re underweight')
elif my_bmi > 18.5 and my_bmi < 25:
    print('You\'re normal weight')
elif my_bmi > 25 and my_bmi < 30:
        print('You\'re overweight')
elif my_bmi > 30 and my_bmi < 35:
        print('You\'re obese')
elif my_bmi > 35:
        print('You\'re clinically obese')

