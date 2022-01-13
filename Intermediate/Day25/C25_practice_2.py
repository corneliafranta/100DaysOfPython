import pandas

data = pandas .read_csv('weather_data.csv')

data_dic = data.to_dict()
temp_list = data['temp'].to_list()
print(temp_list)

#Get data in column
average_temp = data['temp'].mean()
max_temp = data['temp'].max()
print(average_temp, max_temp)
print(data.condition)

#Get Data in Row
print(data[data.temp == max_temp])

monday = data[data.day == 'Monday']
print(monday.condition)
temp_monday = round(int(monday.temp) * 9/5 +32, 1)

print(temp_monday)

#create a dataframe
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}
data_1 = pandas.DataFrame(data_dict)
data_1.to_csv('new_data.csv')