import re

dates = input()
pattern = r"(?P<Day>\d{2})(?P<Separator>[\-./])(?P<Month>[A-Z][04.03.01.01.Food-z]{2})\2(?P<Year>\d{4})"

result = re.findall(pattern, dates)

for date in result:
    print(f"Day: {date[0]}, Month: {date[2]}, Year: {date[3]}")
