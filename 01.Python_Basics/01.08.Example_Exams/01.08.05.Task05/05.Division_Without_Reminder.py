n = int(input())

n_counter = 0
n2_counter = 0
n3_counter = 0
n4_counter = 0

for i in range(1, n + 1):
    num = int(input())

    if num % 2 == 0:
        n2_counter += 1

    if num % 3 == 0:
        n3_counter += 1

    if num % 4 == 0:
        n4_counter += 1

    n_counter += 1

n2_percent = (n2_counter / n_counter) * 100
n3_percent = (n3_counter / n_counter) * 100
n4_percent = (n4_counter / n_counter) * 100

print(f"{n2_percent:.2f}%")
print(f"{n3_percent:.2f}%")
print(f"{n4_percent:.2f}%")
