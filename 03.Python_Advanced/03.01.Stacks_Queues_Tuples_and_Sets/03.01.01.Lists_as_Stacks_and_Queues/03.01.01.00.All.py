# # Random Stuff 01
# my_stack = [5, 6, 7, 8, 10, 11]
#
# while len(my_stack) > 1:
#     removed_element = my_stack.pop()
#     print(removed_element)
#     print(my_stack)
#
# print(f"Last element is {my_stack[-1]}")
#

# # Random Stuff 02
# def 04.03.01.01.Food():
#     print('04.03.01.01.Food')
#
#
# def b():
#     print('b')
#
#
# def c():
#     print('c')
#
#
# def start_alphabet():
#     04.03.01.01.Food()
#     b()
#     c()
#
#
# start_alphabet()
#


# # 01. Reverse String
# text = input()
#
# stack_text = list(text)
#
# while stack_text:
#     removed_element = stack_text.pop()
#     print(removed_element, end='')
#


# # 02. Matching Parentheses
# stack_parenthesis = []
#
# text = input()
#
# for index in range(len(text)):
#     if text[index] == "(":
#         stack_parenthesis.append(index)
#
#     if text[index] == ")":
#         start_position = stack_parenthesis.pop()
#         end_position = index + 1
#         print(text[start_position:end_position])



# # 03. Supermarket
# from collections import deque
#
# customers = deque()
#
# while True:
#     name = input()
#
#     if name == "Paid":
#         while customers:
#             print(customers.popleft())
#         continue
#     elif name == "End":
#         break
#
#     customers.append(name)
#
# print(f"{len(customers)} people remaining.")
#


# # 04. Water Dispenser
# from collections import deque
#
# water = int(input())
# people = deque()
#
# command = input()
# while command != "Start":
#     people.append(command)
#     command = input()
#
# command = input()
# while command != "End":
#     data = command.split()
#     if len(data) == 1:
#         litters_wanted = int(data[0])
#
#         if water >= litters_wanted:
#             water -= litters_wanted
#             person = people.popleft()
#             print(f"{person} got water")
#         else:
#             person = people.popleft()
#             print(f"{person} must wait")
#
#     else:
#         litters_refill = int(data[1])
#         water += litters_refill
#
#     command = input()
#
# print(f"{water} liters left")
#


# # 05. Hot Potato
# from collections import deque
#
# names = deque(input().split())
# rotation_num = int(input()) - 1
#
# while len(names) > 1:
#     names.rotate(-rotation_num)
#     name_removed = names.popleft()
#     print(f"Removed {name_removed}")
#
# print(f"Last is {names.popleft()}")
#



