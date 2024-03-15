# # 01. Numbers Dictionary
# numbers_dictionary = {}
#
# line = input()
# while line != "Search":
#     number_as_string = line
#     try:
#         number = int(input())
#         numbers_dictionary[number_as_string] = number
#     except ValueError:
#         print("The variable number must be an integer")
#
#     line = input()
#
# line = input()
# while line != "Remove":
#     searched = line
#     try:
#         print(numbers_dictionary[searched])
#     except KeyError:
#         print("Number does not exist in dictionary")
#
#     line = input()
#
# line = input()
# while line != "End":
#     searched = line
#     try:
#         del numbers_dictionary[searched]
#     except KeyError:
#         print("Number does not exist in dictionary")
#     line = input()
#
# print(numbers_dictionary)
#


# # 02. Email Validator
# from re import findall
#
#
# class NameTooShortError(Exception):
#     pass
#
#
# class MustContainAtSymbolError(Exception):
#     pass
#
#
# class InvalidDomainError(Exception):
#     pass
#
#
# class MoreThanOneAtSymbolError(Exception):
#     pass
#
#
# class InvalidNameError(Exception):
#     pass
#
#
# MIN_LENGTH = 4
#
# VALID_DOMAINS = ['.com', '.bg', '.org', '.net']
#
# pattern_name = r'[\w]+'
# pattern_domain = r'/.[04.03.01.01.Food-z]+'
#
# email = input()
#
# while email != "End":
#     if email.count("@") > 1:
#         raise MoreThanOneAtSymbolError("Email should contain only 1 @ symbol!")
#     elif email.count("@") < 1:
#         raise MustContainAtSymbolError("Email must contain @!")
#
#     if len(email.split("@")[0]) < MIN_LENGTH:
#         raise NameTooShortError("Name must be more than 4 characters")
#
#     if findall(pattern_name, email)[0] != email.split("@")[0]:
#         raise InvalidNameError("Name can contain only letter, digits and underscores!")
#
#     if findall(pattern_domain, email)[-1] not in VALID_DOMAINS:
#         raise InvalidNameError("Domain must be one of the following: .com, .bg, .org, .net")
#     # if VALID_DOMAINS not in email:
#     #     raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
#
#     print("Email is valid")
#
#     email = input()
#

