from ex29data import menu, resources

turn_off = False
profit = 0
my_profit = 0
is_depleted = False

def print_stock():
    for key, value in resources.items():
        print(f'There\'s {value} of {key} left')

def check_resources(choice):
    for key, value in menu[choice]['ingredients'].items():
        if value <= resources[key]:
            resources[key] = resources[key]-value
            return True
        else:
            print(f'Sorry there is not enough {key}')
            return False

def process_coins(choice, q, d, n , p):
    inserted = 0.25 * q + 0.1 * d + 0.05 * n + 0.01 * p
    total = inserted - menu[choice]['cost']
    return round(total, 2)

def credit_machine(amount, my_profit):
    my_profit += amount
    return my_profit

while turn_off == False:
    my_choice = input('What would you like? (espresso/latte/cappuccino): ')
    if my_choice == 'off':
        print('The machine will shutdown')
        break
    elif my_choice == 'report':
        print_stock()
        print(f'Money: {my_profit}')
    elif my_choice == 'espresso' or my_choice == 'latte' or my_choice == 'cappuccino':
        if check_resources(my_choice) == True:
            print('Please insert coins.')
            my_quarter = int(input('how many quarters?:'))
            my_dime = int(input('how many dimes?:'))
            my_nickle = int(input('how many nickles?:'))
            my_penny = int(input('how many pennies?:'))
            my_result = process_coins(my_choice, my_quarter, my_dime, my_nickle, my_penny)
            if my_result < 0:
                print('Sorry that\'s not enough money. Money refunded.')
            else:
                my_profit = credit_machine(menu[my_choice]['cost'], my_profit)
                print(f'Here is ${my_result} in change.')
                print(f'Here is your {my_choice}. Enjoy!')
        else:
            break
    else:
        continue





