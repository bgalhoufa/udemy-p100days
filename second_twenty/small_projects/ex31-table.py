from prettytable import PrettyTable

my_pokemon = [{'name':'Pikachu','type':'electric'}, {'name':'Squirtle','type':'Water'}, {'name':'Charmander','type':'Fire'}]
table = PrettyTable()

table.field_names = ['Pokemon Names', 'Type']

for i in range(3):
    table.add_row([my_pokemon[i]['name'], my_pokemon[i]['type']])

# Columns left aligned
table.align = 'l'

# We can add a table in another way
# table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
# table.add_column('Type', ['Electric', 'Water', 'Fire'])

#table = PrettyTable.add_row([Pokemon Name', my_pokemon[0]['name']])

print(table)

