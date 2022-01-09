import csv
import pandas

temperatures = []
with open('weather_data.csv') as weather_data_file:
    data =csv.reader(weather_data_file)
    for row in data:
        if  row[1] != 'temp' :
            temperatures.append(int(row[1]))

data = pandas.read_csv('weather_data.csv')
print(data['temp'])



