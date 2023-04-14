sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

my_list = sentence.split()

result = {word:len(word) for word in my_list}


print(result)