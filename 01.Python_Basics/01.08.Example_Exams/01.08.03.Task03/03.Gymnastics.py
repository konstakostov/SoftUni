country = input()
device = input()

difficulty = 0
performance = 0

if country == "Russia":
    if device == "ribbon":
        difficulty = 9.100
        performance = 9.400
    elif device == "hoop":
        difficulty = 9.300
        performance = 9.800
    elif device == "rope":
        difficulty = 9.600
        performance = 9.000

elif country == "Bulgaria":
    if device == "ribbon":
        difficulty = 9.600
        performance = 9.400
    elif device == "hoop":
        difficulty = 9.550
        performance = 9.750
    elif device == "rope":
        difficulty = 9.500
        performance = 9.400

elif country == "Italy":
    if device == "ribbon":
        difficulty = 9.200
        performance = 9.500
    elif device == "hoop":
        difficulty = 9.450
        performance = 9.350
    elif device == "rope":
        difficulty = 9.700
        performance = 9.150

grade = difficulty + performance
percent_for_max = ((20 - grade) / 20) * 100

print(f"The team of {country} get {grade:.3f} on {device}.")
print(f"{percent_for_max:.2f}%")
