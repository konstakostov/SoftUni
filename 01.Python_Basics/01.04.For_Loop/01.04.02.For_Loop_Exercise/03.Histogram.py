n = int(input())

p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0

for i in range(n):
    num = int(input())

    if num < 200:
        p1 += 1
    elif num < 400:
        p2 += 1
    elif num < 600:
        p3 += 1
    elif num < 800:
        p4 += 1
    elif num >= 800:
        p5 += 1

print(f"{p1 / n * 100:.2f}%")
print(f"{p2 / n * 100:.2f}%")
print(f"{p3 / n * 100:.2f}%")
print(f"{p4 / n * 100:.2f}%")
print(f"{p5 / n * 100:.2f}%")
