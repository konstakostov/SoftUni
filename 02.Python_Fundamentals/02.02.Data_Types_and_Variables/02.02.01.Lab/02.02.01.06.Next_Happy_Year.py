year = int(input())

str_year = str(year)

while len(str_year) != len(set(str_year)):
    year += 1
    str_year = str(year)

print(year)
