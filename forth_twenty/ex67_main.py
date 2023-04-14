import pandas

data = pandas.read_csv('nato_alpha.csv')



# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()


#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

new_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

my_name = input('Type a name: ').upper()

my_list = [new_dict[letter] for letter in my_name]

print(my_list)