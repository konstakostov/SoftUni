students = int(input())
lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
max_lectures = 0

for i in range(students):
    attendance = int(input())
    total_bonus = round((attendance / lectures) * (5 + additional_bonus))

    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_lectures = attendance

print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {max_lectures} lectures.")
