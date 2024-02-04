num_students = int(input())

students = {}

for _ in range(num_students):
    name, grade = tuple(input().split())
    grade = float(grade)

    if name not in students:
        students[name] = []

    students[name].append(grade)

# print(students)
for student, grades in students.items():
    average = sum(grades) / len(grades)
    print(f"{student} -> {' '.join([str(f'{grade:.2f}') for grade in grades])} (avg: {average:.2f})")
