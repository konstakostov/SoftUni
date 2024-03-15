def forecast(*args):
    result = ""

    locations = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": [],
    }

    for arg in args:
        city, weather = arg[0], arg[1]
        locations[weather].append(city)

    for key in locations:
        locations[key] = sorted(locations[key])

    for key, value in locations.items():
        if key:
            for city in value:
                result += f"{city} - {key}\n"

    return result.strip()


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print()

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print()

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
