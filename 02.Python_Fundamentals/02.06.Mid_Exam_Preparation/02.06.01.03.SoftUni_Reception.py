employee_01 = int(input())
employee_02 = int(input())
employee_03 = int(input())
students = int(input())

students_hour = employee_01 + employee_02 + employee_03
hours = 0

while True:
    if students <= 0:
        break
    students -= students_hour
    hours += 1
    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")
