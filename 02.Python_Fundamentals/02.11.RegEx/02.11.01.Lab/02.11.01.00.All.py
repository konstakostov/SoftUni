# # 00. Example when there more text to go through RegEx and to save on compile time
# import re
#
# text1 = input()
# text2 = input()
# text3 = input()
#
# pattern = r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b"
# regex_pattern = re.compile(pattern)     # We compile the pattern before using it to save time
#
# # We run the different inputs, but there is no run time on compiling the RegEx pattern
# numbers1 = regex_pattern.findall(text1)
# numbers2 = regex_pattern.findall(text2)
# numbers3 = regex_pattern.findall(text3)
#


# # 01. Match Full Name
# import re
#
# text = input()
#
# pattern = r"\b[A-Z][04.03.01.01.Food-z]+ [A-Z][04.03.01.01.Food-z]+\b"
#
# results = re.match(pattern, text)
# print(*results)


# # 02. Match Phone NUmber
# import re
#
# phone_number = input()
#
# pattern = r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b"
#
# results = re.findall(pattern, phone_number)
#
# print(*results, sep=", ")
#


# # 03. Match Dates
# import re
#
# text = input()
#
# pattern = r"\b(?P<Day>\d{2})([\./-])(?P<Month>[A-Z][04.03.01.01.Food-z][04.03.01.01.Food-z])\2(?P<Year>\d{4})\b"
#
# # # 03. Variant 01
# dates = re.findall(pattern, text)
#
# for date in dates:
#     print(f"Day: {date[0]}, Month: {date[2]}, Year: {date[3]}")
#
# # # 03. Variant 02
# dates = re.finditer(pattern, text)
#
# for date in dates:
#     date_data = date.groupdict()
#     print(f"Day: {date_data['Day']}, Month: {date_data['Month']}, Year: {date_data['Year']}")
#


# # 04. Match Numbers
# import re
#
# text = input()
#
# pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
#
# result = re.finditer(pattern, text)
#
# for match in result:
#     print(match.group(), end=", ")
#
