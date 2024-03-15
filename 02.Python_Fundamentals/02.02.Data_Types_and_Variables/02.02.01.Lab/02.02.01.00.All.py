# # 01. ConCat Names
# first_name = input()
# last_name = input()
# delimeter = input()
#
# print(f"{first_name}{delimeter}{last_name}")
#
#
# # 02. Convert Meters to Kilometers
# meter = int(input())
#
# km = meter / 1000
#
# print(f"{km:.2f}")
#
#
#
# # 03. Pounds to Dollars
# pound = int(input())
#
# usd = pound * 1.31
#
# print(f"{usd:.3f}")
#
#
#
# # 04. Centuries to Minutes
# centuries = int(input())
#
# years = centuries * 100
#
# days = int(years * 365.2422)
#
# hours = days * 24
#
# minutes = hours * 60
#
# print(f"{centuries} centuries = "
#       f"{years} years = "
#       f"{days} days = "
#       f"{hours} hours = "
#       f"{minutes} minutes")
#
#
#
# # 05. Special Numbers
# n = int(input())
#
# for num in range(1, n + 1):
#
#     str_num = str(num)
#
#     sum_symbol = 0
#
#     for symbol in str_num:
#         sum_symbol += int(symbol)
#
#     if sum_symbol == 5 or sum_symbol == 7 or sum_symbol == 11:
#         print(f"{num} -> True")
#     else:
#         print(f"{num} -> False")
#
#
#
# # 06. Next Happy Year
# year = int(input())
# str_year = str(year)
#
# while len(str_year) != len(set(str_year)):
#     year += 1
#     str_year = str(year)
#
# print(year)
#
