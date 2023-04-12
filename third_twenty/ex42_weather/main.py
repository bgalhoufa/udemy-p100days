import pandas

tt_temp = 0
data = pandas.read_csv('weather_data.csv')

#print(data)

# data_list = (data['temp'].tolist())
# print(data_list)
#
print(data[data.temp == data.temp.max()])

