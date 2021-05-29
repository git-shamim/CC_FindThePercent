
n = int(input())
students = []

for i in range(n):
    student = input().split()
    students.append(student)

query_name = input()

total_marks = 0
num_subjects = 0

for student in students:
    name = student[0].lower()
    if name == query_name.lower():
        for i in range(1, len(student)):
            total_marks += float(student[i])
            num_subjects += 1

average_marks = total_marks / num_subjects
print("{0:.2f}".format(average_marks))

