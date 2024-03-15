# # 01. Valid Usernames
# def length_is_valid(name):
#     if 3 <= len(name) <= 16:
#         return True
#     return False
#
#
# def characters_are_valid(name):
#     for char in name:
#         if not (char.isalnum() or char == "_" or char == "-"):
#             return False
#     return True
#
#
# def no_redundant_symbols(name):
#     if " " in name:
#         return False
#     return True
#
#
# def username_validation(name):
#     if length_is_valid(name) and characters_are_valid(name) and no_redundant_symbols(name):
#         return True
#     return False
#
#
# usernames = input().split(", ")
#
# for username in usernames:
#     if username_validation(username):
#         print(username)
#


# # 02. Character Multiplier
# string1, string2 = input().split()
#
# total_sum = 0
#
# if len(string1) > len(string2):
#     for index in range(len(string2)):
#         total_sum += ord(string1[index]) * ord(string2[index])
#     for index in range(len(string2), len(string1)):
#         total_sum += ord(string1[index])
#
# elif len(string1) < len(string2):
#     for index in range(len(string1)):
#         total_sum += ord(string1[index]) * ord(string2[index])
#     for index in range(len(string1), len(string2)):
#         total_sum += ord(string2[index])
#
# else:
#     for index in range(len(string1)):
#         total_sum += ord(string1[index]) * ord(string2[index])
#
# print(total_sum)
#


# 03. Extract File


# 04. Caesar Cipher


# 05. Emoticon Finder


# # 06. Replace Repeating Chars
# text = input()
#
# new_text = ""
# last_letter = ""
#
# for current_letter in text:
#     if last_letter != current_letter:
#         new_text += current_letter
#         last_letter = current_letter
#
# print(new_text)

# # 07. String Explosion
# text = input()
# new_text = ""
# strength = 0
#
# for i in range(len(text)):
#     if strength > 0 and text[i] != ">":
#         strength -= 1
#     elif text[i] == ">":
#         new_text += text[i]
#         strength += int(text[i + 1])
#     else:
#         new_text += text[i]
#
# print(new_text)
#


# 08. *Letters Change Numbers


# 09. *Rage Quit


# 10. *Winning Ticket

