# Students which have taken the Exam
students = int(input())

# Grades
grade_2 = 0     # Grade Between 2.00 and 2.99
grade_3 = 0     # Grade Between 3.00 and 3.99
grade_4 = 0     # Grade Between 4.00 and 4.99
grade_5 = 0

grades_sum = 0

# Logic
for _ in range(1, students + 1):
    grade = float(input())          # Grade of Each Student

    if 2 <= grade <= 2.99:          # Grade Between 2.00 and 2.99
        grade_2 += 1
        grades_sum += grade
    elif 3 <= grade <= 3.99:        # Grade Between 3.00 and 3.99
        grade_3 += 1
        grades_sum += grade
    elif 4 <= grade <= 4.99:        # Grade Between 4.00 and 4.99
        grade_4 += 1
        grades_sum += grade
    else:                             # Grade Above 5.00
        grade_5 += 1
        grades_sum += grade

# Percentage
grade_2_perc = (grade_2 / students) * 100       # Failed Students
grade_3_perc = (grade_3 / students) * 100       # Between 3.00 and 3.99
grade_4_perc = (grade_4 / students) * 100       # Between 4.00 and 4.99
grade_5_perc = (grade_5 / students) * 100       # Top students

# Average Score
grade_average = grades_sum / students

# Printed Results
print(f"Top students: {grade_5_perc:.2f}%")
print(f"Between 4.00 and 4.99: {grade_4_perc:.2f}%")
print(f"Between 3.00 and 3.99: {grade_3_perc:.2f}%")
print(f"Fail: {grade_2_perc:.2f}%")
print(f"Average: {grade_average:.2f}")
