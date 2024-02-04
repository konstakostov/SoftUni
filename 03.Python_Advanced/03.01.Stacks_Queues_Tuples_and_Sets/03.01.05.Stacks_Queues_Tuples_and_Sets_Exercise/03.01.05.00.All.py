# # 01. Numbers, Version 01
# first = set(int(x) for x in input().split())
# second = set(int(x) for x in input().split())
#
# for _ in range(int(input())):
#     first_command, second_command, *data = input().split()
#
#     command = first_command + " " + second_command
#
#     if command == "Add First":
#         [first.add(int(el)) for el in data]
#
#     elif command == "Add Second":
#         [second.add(int(el)) for el in data]
#
#     elif command == "Remove First":
#         # Discard does not give error if element does not exist, unlike Remove
#         [first.discard(int(el)) for el in data]
#
#     elif command == "Remove Second":
#         [second.discard(int(el)) for el in data]
#
#     else:
#         print(first.issubset(second) or second.issubset(first))
#
# print(*sorted(first), sep=", ")
# print(*sorted(second), sep=", ")
#

# # 01. Numbers, Version 02
# first = set(int(x) for x in input().split())
# second = set(int(x) for x in input().split())
#
# functions = {
#     "Add First": lambda x: [first.add(el) for el in x],
#     "Add Second": lambda x: [second.add(el) for el in x],
#     "Remove First": lambda x: [first.discard(el) for el in x],
#     "Remove Second": lambda x: [second.discard(el) for el in x],
#     "Check Subset": lambda x: print(first.issubset(second) or second.issubset(first)),
# }
#
# for _ in range(int(input())):
#     first_command, second_command, *data = input().split()
#     command = first_command + " " + second_command
#
#     functions[command](int(x) for x in data)
#
# print(*sorted(first), sep=", ")
# print(*sorted(second), sep=", ")
#


# # 02. Expression Evaluator, Version 01
# from collections import deque
# from math import floor
#
# expression = deque(input().split())
#
# index = 0
#
# while index < len(expression):
#     element = expression[index]
#
#     if element == "*":
#         for _ in range(index - 1):
#             expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
#
#     elif element == "/":
#         for _ in range(index - 1):
#             expression.appendleft(int(expression.popleft()) / int(expression.popleft()))
#
#     elif element == "+":
#         for _ in range(index - 1):
#             expression.appendleft(int(expression.popleft()) + int(expression.popleft()))
#
#     elif element == "-":
#         for _ in range(index - 1):
#             expression.appendleft(int(expression.popleft()) - int(expression.popleft()))
#
#     if element in "*/+-":
#         del expression[1]
#         index = 1
#
#     index += 1
#
# print(floor(int(expression[0])))
#

# # 02. Expression Evaluator, Version 02
# from functools import reduce
# from math import floor
#
# expression = input().split()
#
# index = 0
#
# functions = {
#     "*": lambda i: reduce(lambda 04.03.01.01.Food, b: 04.03.01.01.Food * b, map(int, expression[:i])),
#     "/": lambda i: reduce(lambda 04.03.01.01.Food, b: 04.03.01.01.Food / b, map(int, expression[:i])),
#     "+": lambda i: reduce(lambda 04.03.01.01.Food, b: 04.03.01.01.Food + b, map(int, expression[:i])),
#     "-": lambda i: reduce(lambda 04.03.01.01.Food, b: 04.03.01.01.Food - b, map(int, expression[:i]))
# }
#
# while index < len(expression):
#     element = expression[index]
#
#     if element in "*/+-":
#         expression[0] = functions[element](index)
#         [expression.pop(1) for i in range(index)]
#         index = 1
#
#     index += 1
#
# print(floor(int(expression[0])))
#


# # 03. Milkshakes
# from collections import deque
#
# chocolates = deque(int(x) for x in input().split(', '))
# milk_cups = deque(int(x) for x in input().split(', '))
#
# milkshakes = 0
#
# while milkshakes != 5 and chocolates and milk_cups:
#     chocolate = chocolates.pop()
#     milk_cup = milk_cups.popleft()
#
#     if chocolate <= 0 and milk_cup <= 0:
#         continue
#     elif chocolate <= 0:
#         milk_cups.appendleft(milk_cup)
#         continue
#     elif milk_cup <= 0:
#         chocolates.append(chocolate)
#         continue
#
#     if chocolate == milk_cup:
#         milkshakes += 1
#     else:
#         milk_cups.append(milk_cup)
#         chocolates.append(chocolate - 5)
#
# if milkshakes == 5:
#     print(f"Great! You made all the chocolate milkshakes needed!")
# else:
#     print(f"Not enough milkshakes.")
#
# print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
# print(f"Milk: {', '.join(str(x) for x in milk_cups) or 'empty'}")
#


# # 04. Honey
# from collections import deque
#
# bees = deque(int(x) for x in input().split())
# nectar = deque(int(x) for x in input().split())
# symbols = deque(x for x in input().split())
#
# honey = 0
#
# operations = {
#     "*": lambda x, y: x * y,
#     "/": lambda x, y: x / y,
#     "+": lambda x, y: x + y,
#     "-": lambda x, y: x - y
# }
#
# while bees and nectar:
#     current_bee = bees.popleft()
#     current_nectar = nectar.pop()
#
#     if current_nectar < current_bee:
#         bees.appendleft(current_bee)
#     elif current_nectar > current_bee:
#         honey += abs(operations[symbols.popleft()](current_bee, current_nectar))
#
# print(f"Total honey made: {honey}")
#
# if bees:
#     print(f"Bees left: {', '.join(str(x) for x in bees)}")
#
# if nectar:
#     print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
#


# # 05. Santa's Present Factory
# from collections import deque
#
# materials = deque(int(x) for x in input().split())
# magic_levels = deque(int(x) for x in input().split())
#
# crafted = []
# presents = {
#     150: "Doll",
#     250: "Wooden train",
#     300: "Teddy bear",
#     400: "Bicycle"
# }
#
# while materials and magic_levels:
#     material = materials.pop() if magic_levels[0] or not materials[0] else 0
#     magic_level = magic_levels.popleft() if material or not magic_levels[0] else 0
#
#     if not magic_level:
#         continue
#
#     product = material * magic_level
#
#     if presents.get(product):
#         crafted.append(presents[product])
#     elif product < 0:
#         materials.append(material + magic_level)
#     elif product > 0:
#         materials.append(material + 15)
#
# if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")
#
# if materials:
#     print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")
#
# if magic_levels:
#     print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")
#
# [print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]
#


# # 06. Paint Colors
# from collections import deque
#
# words = deque(input().split())
#
# colors = {'red', 'yellow', 'blue', 'orange', 'purple', 'green'}
# req_colors = {
#     'orange': {'yellow', 'red'},
#     'purple': {'red', 'blue'},
#     'green': {'yellow', 'blue'}
# }
#
# collected_colors = []
#
# while words:
#     first_word = words.popleft()
#     second_word = words.pop() if words else ''
#
#     for color in (first_word + second_word, second_word + first_word):
#         if color in colors:
#             collected_colors.append(color)
#             break
#     else:
#         for el in first_word[:-1], second_word[:-1]:
#             if el:
#                 words.insert(len(words) // 2, el)
#
# for color in set(req_colors.keys()).intersection(collected_colors):
#     if not req_colors[color].issubset(collected_colors):
#         collected_colors.remove(color)
#
# print(collected_colors)
#
