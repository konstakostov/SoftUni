# # Other Stuff
#
# txt_1 = "Welcome to the Jungle"
#
# x = txt_1.split()
#
# print(type(x))
# print(x)
# print(txt_1)
#
# txt_2 = "Welcome         to         the Jungle"
#
# y = txt_2.split(" ")
#
# print(type(y))
# print(y)
# print(txt_2)
#
# txt_3 = "1, 2, 3, 4, 5"
#
# z = txt_3.split(",")
#
# print(type(z))
# print(z)
# print(txt_3)
#
#
#
# # 01. Strange Zoo, Version 01
# tail = input()
# body = input()
# head = input()
#
# meerkat = [tail, body, head]
#
# meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
#
# print(meerkat)
#
#
#
# # 01. Strange Zoo, Version 02
# tail, body, head = input(), input(), input()
#
# meerkat = [tail, body, head]
# meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
#
# print(meerkat)
#
#
#
# # 02. Courses
# num = int(input())
#
# courses = []
#
# for i in range(num):
#     current_course = input()
#     courses.append(current_course)
#
# print(courses)
#
#
#
# # 03. 04.10.01.03.List Statistics
# n = int(input())
#
# positive_lst = []
# negative_lst = []
#
# for i in range(n):
#     num = int(input())
#
#     if num > 0:
#         positive_lst.append(num)
#     elif num < 0:
#         negative_lst.append(num)
#
# print(positive_lst)
# print(negative_lst)
# print(f"Count of positives: {len(positive_lst)}")
# print(f"Sum of negatives: {sum(negative_lst)}")
#
#
#
# # 04. Search
# n = int(input())
# word = input()
#
# lst = []
#
# for i in range(n):
#     current_str = input()
#
#     lst.append(current_str)
#
# print(lst)
#
# for i in range(len(lst) -1, -1, -1):
#     element = lst[i]
#     if word not in element:
#         lst.remove(element)
#
# print(lst)
#
#
#
# # 05. Numbers Filter
# n = int(input())
#
# numbers_lst = []
#
# even = []
# odd = []
# negative = []
# positive = []
#
# for i in range(n):
#     num = int(input())
#
#     numbers_lst.append(num)
#
# for i in range(0, len(numbers_lst)):
#     current_num = numbers_lst[i]
#
#     if current_num % 2 == 0 or current_num == 0:
#         even.append(current_num)
#     elif current_num % 2 != 0:
#         odd.append(current_num)
#
#     if current_num >= 0:
#         positive.append(current_num)
#     else:
#         negative.append(current_num)
#
# command = input()
#
# if command == "even":
#     print(even)
#
# elif command == "odd":
#     print(odd)
#
# elif command == "negative":
#     print(negative)
#
# elif command == "positive":
#     print(positive)
#
