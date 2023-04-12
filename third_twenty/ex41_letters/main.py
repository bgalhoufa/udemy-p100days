#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('Input/Letters/starting_letter.txt') as letter:
    my_letter = letter.readlines()

with open('Input/Names/invited_names.txt') as names:
    my_names = names.readlines()


new_names =[]

for name in my_names:
    new_names.append(name.replace('\n', ''))

my_sub = my_letter[0]
my_new_letter = "".join(my_letter[1:])

for name in new_names:
    my_name = my_sub.replace('[name]', name)
    my_join_letter = my_name + my_new_letter
    print(my_join_letter)
    with open(f'Output/ReadyToSend/{name}.txt', mode='w') as fw:
        fw.write(my_join_letter)




