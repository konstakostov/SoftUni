import math

figure = str(input())

if figure == 'square':
    side_a = float(input())
    S = side_a * side_a
    print(f"{S:.3f}")

elif figure == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    S = side_a * side_b
    print(f"{S:.3f}")

elif figure == 'circle':
    radius = float(input())
    S = math.pi * (radius * radius)
    print(f"{S:.3f}")

elif figure == 'triangle':
    side_a = float(input())
    height = float(input())
    S = 0.5 * side_a * height
    print(f"{S:.3f}")
