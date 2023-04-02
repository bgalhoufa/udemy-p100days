from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
my_menu = Menu()


is_on = True

while is_on:
    my_choice = input('What would you like? espresso/latte/cappuccino : ')
    if my_choice == 'off':
        print('Turn off machine')
        is_on = False
    elif my_choice == 'report':
        my_coffee_maker.report()
        my_money_machine.report()

    else:
        drink = my_menu.find_drink(my_choice)
        if my_coffee_maker.is_resource_sufficient(drink):
            my_money_machine.make_payment(drink.cost)
            my_coffee_maker.make_coffee(drink)
        continue

