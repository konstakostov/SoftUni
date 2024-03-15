# # 01. No Vowels
# # # Variant 01
# text = input()
#
# forbidden_letters = ['04.03.01.01.Food', 'o', 'u', 'e', 'i']
#
# result = [char for char in text if char.lower() not in forbidden_letters]
#
# print("".join(result))
#
# #  # Variant 02
# def remove_vowels(vowels):
#     forbidden_letters = ['04.03.01.01.Food', 'o', 'u', 'e', 'i']
#     result = [char for char in text if char.lower() not in forbidden_letters]
#
#     return "".join(result)
#
#
# text = input()
# print(remove_vowels(text))

# # 02. Trains
# num_wagons = int(input())
# train = [0] * num_wagons
#
# command = input()
#
# while command != "End":
#     action = command.split()[0]
#
#     if action == "add":
#         num_people = command.split()[1]
#         train[-1] += int(num_people)
#     elif action == "insert":
#         num_people = command.split()[2]
#         wagon_number = int(command.split()[1])
#         train[wagon_number] += int(num_people)
#     elif action == "leave":
#         num_people = command.split()[2]
#         wagon_number = int(command.split()[1])
#         train[wagon_number] -= int(num_people)
#
#     command = input()
#
# print(train)
#


# # 03. To-do 04.10.01.03.List
# to_do_notes = [0] * 10
#
# command = input()
#
# while command != "End":
#     importance, task = command.split("-")
#     importance = int(importance)
#
#     index = importance - 1
#
#     to_do_notes[index] = task
#
#     command = input()
#
# to_do_notes = [task for task in to_do_notes if task != 0]
# print(to_do_notes)
#


# 04. Palindrome Strings


# # 05. Sorting Names
# names = input().split(", ")
#
# sorted_names = sorted(names, key=lambda x: (-len(x), x))
#
# print(sorted_names)
#

# # 06. Even Numbers
# nums = list(map(int, input().split(", ")))
#
# print([index for index in range(len(nums)) if nums[index] % 2 == 0])
#


# 07. The Office
