import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_squirrles_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrles_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_suirrles_count = len(data[data['Primary Fur Color'] == 'Black'])

new_data = {'type': ['grey', 'cinnamon', 'black'], 'amount': [grey_squirrles_count, cinnamon_squirrles_count, black_suirrles_count]}

data_1 = pandas.DataFrame(new_data)
data_1.to_csv('squirrle_data.csv')