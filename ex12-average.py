#/usr/bin/env python3

student_heights = input('Input a list of student heights ').split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total = 0

for item in student_heights:
    total = total + item

average = total / len(student_heights)

print(average)
