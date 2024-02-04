# # 01. Bakery
# data = input().split()
# bakery = {}
#
# for i in range(0, len(data), 2):
#     key = data[i]
#     value = int(data[i + 1])
#     bakery[key] = value
#
# print(bakery)
#


# # 02. Stock
# data = input().split()
# searched_product = input().split()
#
# bakery = {}
#
# for i in range(0, len(data), 2):
#     key = data[i]
#     value = int(data[i + 1])
#     bakery[key] = value
#
# for product in searched_product:
#     if product in bakery:
#         print(f"We have {bakery[product]} of {product} left")
#     else:
#         print(f"Sorry, we don't have {product}")
#


# # 03. Statistics
# bakery = {}
#
# data = input()
#
# while data != "statistics":
#     tokens = data.split(": ")
#     product = tokens[0]
#     quantity = int(tokens[1])
#
#     if product not in bakery:
#         bakery[product] = 0
#
#     bakery[product] += quantity
#
#     data = input()
#
# print("Products in stock:")
# for product, quantity in bakery.items():
#     print(f"{product}: {quantity}")
# print(f"Total Products: {len(bakery.keys())}")
# print(f"Total Quantity: {sum(bakery.values())}")
#


# # 04. Students
# data = input()
#
# courses = {}
#
# while ":" in data:
#     student_name, student_id, course_name = data.split(":")
#     if course_name not in courses:
#         courses[course_name] = {student_id: student_name}
#     else:
#         courses[course_name][student_id] = student_name
#
#     data = input()
#
# course_name = data.replace("_", " ")
# students = courses[course_name]
#
# for student_id, name in students.items():
#     print(f"{name} - {student_id}")
#


# # 05. ASCII Values, Variant 01
# characters = input().split(", ")
# print({char: ord(char) for char in characters})
#
# # 05. ASCII Values, Variant 02
# print({char: ord(char) for char in input().split(", ")})
#


# # 06. Odd Occurrences
# words_key = [el.lower() for el in input().split()]
# default = 0
#
# occurrences = dict.fromkeys(words_key, default)
#
# for word in words_key:
#     occurrences[word] += 1
#
# for word, count in occurrences.items():
#     if count % 2 != 0:
#         print(word, end=" ")
#


# # 07. Word Synonyms
# word_count = int(input())
# synonyms = {}
#
# for i in range(word_count):
#     key = input()
#     value = input()
#
#     if key not in synonyms:
#         synonyms[key] = []
#
#     synonyms[key].append(value)
#
# print(synonyms)
#
# for word, all_synonyms in synonyms.items():
#     print(f"{word} - {', '.join(all_synonyms)}")
#
