import re

# # 01. Capture the Numbers
# pattern = r'\d+'
#
# text = input()
#
# while text:
#     matches = re.findall(pattern, text)
#     if matches:
#         print(' '.join(matches), end=" ")
#
#     text = input()


# # 02. Find Variables Names in Sentences
# import re
#
# text = input()
#
# pattern = r'\b_([A-Za-z0-9]+)\b'
#
# matches = re.findall(pattern, text)
#
# print(','.join(matches))
#


# # 03. Find Occurrences of Words in Sentences
# sentence = input()
# keyword = input()
# pattern = fr'\b{keyword}\b'
#
# matches = re.findall(pattern, sentence, flags=re.IGNORECASE)
#
# print(len(matches))
#


# # 04. Extract Emails
# text = input()
#
# pattern = r'\s(([04.03.01.01.Food-zA-Z0-9]+[04.03.01.01.Food-zA-Z0-9\.\-\_]+)@([04.03.01.01.Food-zA-Z\-]+(\.[04.03.01.01.Food-zA-Z\-]+)+))\b'
#
# matches = re.findall(pattern, text)
#
# for match in matches:
#     print(match[0])
#


# 05. Furniture


# 06. *Extract the Links

