name = input()

grades_sum = 0
bad_grades = 0
current_year = 0

while True:
    grade = float(input())

    if grade < 4:
        bad_grades += 1
        if bad_grades >= 2:
            break
        continue

    grades_sum += grade
    current_year += 1

    if current_year >= 12:
        break

average_grade = grades_sum / 12

if bad_grades >= 2:
    print(f"{name} has been excluded at {current_year + 1} grade")
else:
    print(f"{name} graduated. Average grade: {grades_sum / 12:.2f} ")

