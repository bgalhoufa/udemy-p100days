#/usr/bin/env python3

student_scores = input('Input a list of student scores ').split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

student_scores.sort()

print(student_scores[-1])
