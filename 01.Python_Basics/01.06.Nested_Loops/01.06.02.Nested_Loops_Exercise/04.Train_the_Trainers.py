judges = int(input())

total_grades_sum = 0
total_grades_num = 0

while True:
    presentation = input()

    if presentation == "Finish":
        break

    grades_sum = 0

    for i in range(judges):
        grades_sum += float(input())

    total_grades_sum += grades_sum
    total_grades_num += judges

    print(f"{presentation} - {(grades_sum / judges):.2f}.")

print(f"Student's final assessment is {(total_grades_sum / total_grades_num):.2f}.")
