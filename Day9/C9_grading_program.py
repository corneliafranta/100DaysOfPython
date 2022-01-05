student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    grade = ""

    if student_scores[student] > 90:
        grade = "Outstanding"
    elif student_scores[student] > 80:
        grade = "Exceeds Expectations"
    elif student_scores[student] > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"

    student_grades[student] = grade

print(student_grades)