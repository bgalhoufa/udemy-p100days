import random

students = ['Bruno', 'Vasco', 'Lucia', 'Xavier', 'Clara', 'Joao', 'Dina']

dict_grades = {student:random.randint(1, 100) for student in students}

passed_students = {student:grade for student, grade in dict_grades.items() if grade > 50}

print(passed_students)