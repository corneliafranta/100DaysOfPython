student_dict = {
    'students' : ['Angela', 'James', 'Lilly'],
    'score': [56, 76, 98]
}

#Looping through a dictionary
for (key, value) in student_dict.items():
    print(value)

#Looping through a data frame
import pandas
student_data_frame = pandas.DataFrame(student_dict)

#for (key, value) in student_data_frame.items():
#    print(value)

for (index, row) in student_data_frame.iterrows():
    print(row.students)