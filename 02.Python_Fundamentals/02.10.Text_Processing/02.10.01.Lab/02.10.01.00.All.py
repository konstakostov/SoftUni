# # 01. Reverse Strings, Version 01
# while True:
#     word = input()
#     if word == "end":
#         break
#
#     reversed_word = ""
#
#     for char in reversed(word):
#         reversed_word += char
#
#     print(f"{word} = {reversed_word}")
#
# # 01. Reverse Strings, Version 02
# word = input()
#
# while word != "end":
#     print(f"{word} = {word[::-1]}")
#
#     word = input()
#


# # 02. Repeat Strings, Version 01
# words = input().split()
#
# result = [word * len(word) for word in words]
#
# print("".join(result))
#
# # 02. Repeat Strings, Version 02
# result = ""
#
# for word in words:
#     result += word * len(word)
#
# print("".join(result))
#


# # 03. Substring
# first = input()
# second = input()
#
# while first in second:
#     second = second.replace(first, "")
#
# print(second)
#


# # 04. Text_Filter
# banned_words = input().split(", ")
# text = input()
#
# for banned in banned_words:
#     while banned in text:
#         text = text.replace(banned, "*" * len(banned))
#
# print(text)
#


# # 05. Digits, Letters and Others
# text = input()
#
# digits = ""
# letters = ""
# other = ""
#
# for char in text:
#     if char.isdigit():
#         digits += char
#
#     elif char.isalpha():
#         letters += char
#
#     else:
#         other += char
#
# print(digits)
# print(letters)
# print(other)
#
