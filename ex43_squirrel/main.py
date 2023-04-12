import pandas

data = pandas.read_csv('Squirrel_Data.csv')

#print(data[data.X])
c_gray = 0
c_red = 0
c_black = 0

for color in data['Primary Fur Color']:
    if color == 'Gray':
        c_gray += 1
    elif color == 'Black':
        c_black += 1
    elif color == 'Cinnamon':
        c_red += 1

#data_colors = data['Primary Fur Color']

#print(f'There are {c_gray} gray, {c_black} black and {c_red} red squirrels')

my_dict = {
    'Fur Color': ['grey', 'red', 'black'],
    'Count': [c_gray, c_red, c_black]
}

my_data = pandas.DataFrame(my_dict)
print(my_data)
my_data.to_csv('squirrel_count.csv')