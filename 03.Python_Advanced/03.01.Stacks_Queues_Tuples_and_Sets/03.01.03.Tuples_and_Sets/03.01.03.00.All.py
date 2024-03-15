# # 01. Count Same Values, Version 01
# nums = tuple(input().split())
#
# occurrences = {}
#
# for elem in nums:
#     if elem not in occurrences:
#         occurrences[elem] = 0
#     occurrences[elem] += 1
#
# for number, count in occurrences.items():
#     print(f"{float(number):.1f} - {count} times")

# # 01. Count Same Values, Version 02
# nums = tuple([float(num) for num in input().split()])
#
# occurrences = {}
#
# for el in nums:
#     occurrences[el] = nums.count(el)
#
#
# for number, count in occurrences.items():
#     print(f"{float(number):.1f} - {count} times")
#


# # 02. Student's Grades, Version 01
# num_students = int(input())
#
# students = {}
#
# for _ in range(num_students):
#     name, grade = tuple(input().split())
#     grade = float(grade)
#     if name not in students:
#         students[name] = []
#     students[name].append(grade)
#
# for name, grades in students.items():
#     avg = sum(grades) / len(grades)
#     print(f"{name} -> {' '.join([str(f'{grade:.2f}') for grade in grades])} (avg: {avg:.2f})")

# # 02. Student's Grades, Version 02
# from statistics import mean
# from collections import defaultdict
#
# num_students = int(input())
#
# students = defaultdict(lambda: [])
#
# for _ in range(num_students):
#     name, grade = tuple(input().split())
#     grade = float(grade)
#     students[name].append(grade)
#
# for name, grades in students.items():
#     avg = mean(grades)
#     print(f"{name} -> {' '.join([str(f'{grade:.2f}') for grade in grades])} (avg: {avg:.2f})")
#


# # 03. Record Unique Names
# n = int(input())
#
# names = set()
#
# for _ in range(n):
#     name = input()
#     names.add(name)
#
# for name in names:
#     print(name)
#


# # 04. Parking Lot
# num_cars = int(input())
#
# parking_lot = set()
#
# for _ in range(num_cars):
#     direction, car_id = input().split(", ")
#
#     if direction == "IN":
#         parking_lot.add(car_id)
#
#     elif direction == "OUT":
#         parking_lot.remove(car_id)
#
# if parking_lot:
#     print(*parking_lot, sep='\n')
# else:
#     print("Parking Lot is Empty")
#


# # 05. SoftUni Party
# num_guests = int(input())
#
# reservations = set()
#
# for _ in range(num_guests):
#     guest = input()
#     reservations.add(guest)
#
# while True:
#     command = input()
#     if command == "END":
#         break
#
#     # IF statement guarantees it will work if there is input which is not in the Reservations Set;
#     if command in reservations:
#         reservations.remove(command)
#
# print(len(reservations))
# for el in sorted(reservations):
#     print(el)
#


# 06. Summation Pairs

