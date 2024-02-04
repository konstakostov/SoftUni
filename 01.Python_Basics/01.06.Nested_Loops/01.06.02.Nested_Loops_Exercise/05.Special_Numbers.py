num = int(input())

for n in range(1111, 10000):
    for digit in str(n):
        if digit == "0":
            break

        if num % int(digit) != 0:
            break
    else:
        print(n, end=" ")
