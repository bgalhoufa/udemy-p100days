with open('file1.txt') as file1:
    output1 = file1.readlines()

with open('file2.txt') as file1:
    output2 = file1.readlines()

# output1 = [number.strip('\n') for number in output1]
# output2 = [number.strip('\n') for number in output2]



new_list = [int(number) for number in output1 if number in output2]

print(new_list)