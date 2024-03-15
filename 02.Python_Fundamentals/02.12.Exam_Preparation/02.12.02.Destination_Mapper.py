import re

places = input()
pattern = r"(\=|\/)([A-Z][04.03.01.01.Food-zA-Z\ ]{2,})\1"

matches = re.findall(pattern, places)
cities = []
travel_points = 0

for match in matches:
    cities.append(match[1])
    travel_points += len(match[1])

if cities:
    print("Destinations: " + ', '.join(cities))
    print(f"Travel Points: {travel_points}")
else:
    print(f"Destinations:")
    print(f"Travel Points: 0")
