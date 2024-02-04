painted_eggs = int(input())

red_counter = 0
orange_counter = 0
blue_counter = 0
green_counter = 0

max_counter = 0
max_color = ""

for i in range(painted_eggs):
    color = input()

    if color == "red":
        red_counter += 1
        if red_counter > max_counter:
            max_counter = red_counter
            max_color = "red"

    elif color == "orange":
        orange_counter += 1
        if orange_counter > max_counter:
            max_counter = orange_counter
            max_color = "orange"

    elif color == "blue":
        blue_counter += 1
        if blue_counter > max_counter:
            max_counter = blue_counter
            max_color = "blue"

    elif color == "green":
        green_counter += 1
        if green_counter > max_counter:
            max_counter = green_counter
            max_color = "green"

print(f"Red eggs: {red_counter}")
print(f"Orange eggs: {orange_counter}")
print(f"Blue eggs: {blue_counter}")
print(f"Green eggs: {green_counter}")
print(f"Max eggs: {max_counter} -> {max_color}")
