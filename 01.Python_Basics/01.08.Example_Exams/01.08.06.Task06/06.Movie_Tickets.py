a1 = int(input())
a2 = int(input())
n = int(input())

for num1 in range(a1, a2):

    if num1 % 2 == 0:
        continue

    for num2 in range(1, n):
        for num3 in range(1, int(n / 2)):
            num4 = num1

            if (num2 + num3 + num4) % 2 == 0:
                continue

            print(f"{chr(num1)}-{num2}{num3}{num4}")
