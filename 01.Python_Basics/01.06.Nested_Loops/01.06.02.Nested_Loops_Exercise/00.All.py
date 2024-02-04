# # NUMBER PYRAMID
# n = int(input())
#
# counter = 0
#
# for rows in range(1, n + 1):
#     for columns in range(1, rows + 1):
#         counter += 1
#
#         if rows != columns:
#             print(f"{counter}", end=" ")
#         else:
#             print(f"{counter}")
#
#         if counter == n:
#             raise SystemExit
#


# # EQUAL SUMS EVEN ODD POSITIONS
# num1, num2 = int(input()), int(input())
#
# for number in range(num1, num2 + 1):
#     odd_sum, even_sum = 0, 0
#
#     for index, digit in enumerate(str(number)):
#         if index % 2 == 0:
#             even_sum += int(digit)
#         else:
#             odd_sum += int(digit)
#
#     if even_sum == odd_sum:
#         print(number, end=" ")
#


# # SUM PRIME NON PRIME
# sum_prime = 0
# sum_non_prime = 0
#
# while True:
#     command = input()
#
#     if command == "stop":
#         break
#
#     current_num = int(command)
#     is_prime = True
#
#     if current_num < 0:
#         print("Number is negative.")
#         continue
#
#     for number in range(2, current_num):
#         if current_num % number == 0:
#             is_prime = False
#             break
#
#     if is_prime:
#         sum_prime += current_num
#     else:
#         sum_non_prime += current_num
#
# print(f"Sum of all prime numbers is: {sum_prime}")
# print(f"Sum of all non prime numbers is: {sum_non_prime}")
#


# # TRAIN THE TRAINERS
# judges = int(input())
#
# total_grades_num = 0
# total_grades_sum = 0
#
# while True:
#     presentation = input()
#
#     if presentation == "Finish":
#         break
#
#     grade_sum = 0
#
#     for _ in range(judges):
#         grade_sum += float(input())
#
#     total_grades_sum += grade_sum
#     total_grades_num += judges
#
#     print(f"{presentation} - {(grade_sum / judges):.2f}.")
#
# print(f"Student's final assessment is {(total_grades_sum / total_grades_num):.2f}.")
#


# # SPECIAL NUMBERS
# num = int(input())
#
# for n in range(1111, 10000):
#     for digit in str(n):
#         if digit == "0":
#             break
#         if num % int(digit) != 0:
#             break
#
#     else:
#         print(n, end=" ")
#


# # CINEMA TICKETS
# students_total = 0
# standard_total = 0
# kids_total = 0
#
# while True:
#     movie = input()
#
#     if movie == "Finish":
#         break
#
#     capacity = int(input())
#     sold_tickets = 0
#
#     while sold_tickets < capacity:
#         ticket_type = input()
#
#         if ticket_type == "End":
#             break
#
#         if ticket_type == "04.10.02.04.Student":
#             students_total += 1
#         elif ticket_type == "standard":
#             standard_total += 1
#         else:
#             kids_total += 1
#
#         sold_tickets +=1
#
#     print(f"{movie} - {((sold_tickets / capacity) * 100):.2f}% full.")
#
# tickets_total = students_total + standard_total + kids_total
#
# print(f"Total tickets: {tickets_total}")
# print(f"{((students_total / tickets_total) * 100):.2f}% 04.10.02.04.Student tickets.")
# print(f"{((standard_total / tickets_total) * 100):.2f}% standard tickets.")
# print(f"{((kids_total / tickets_total) * 100):.2f}% kids tickets.")
#
