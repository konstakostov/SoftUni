n1 = int(input())
n2 = int(input())
n3 = int(input())

is_prime = True

num1 = 0
num2 = 0
num3 = 0

for x1 in range(1, n1 + 1):
    for x2 in range(1, n2 + 1):
        for x3 in range(1, n3 + 1):

            if n1 % 2 == 0:
                num1 = x1

            if (n2 + 1) % x2 == 0:
                is_prime = False
                break
            if is_prime:
                num2 = x2
            else:
                num2_ignore = x2

            if n3 % 2 == 0:
                num3 = x3
            print(f"{num1} {num2} {num3}")
    print()
