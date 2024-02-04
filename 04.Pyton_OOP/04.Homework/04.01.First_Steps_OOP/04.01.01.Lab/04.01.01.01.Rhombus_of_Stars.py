def print_lines(n, count):
    print(' ' * (n - count), end='')
    print(*['*'] * count)


def triangle(n):
    for count in range(1, n + 1):
        print_lines(n, count)


def reverse_triangle(n):
    for count in range(n - 1, 0, -1):
        print_lines(n, count)


def rhombus(n):
    triangle(n)
    reverse_triangle(n)


num = int(input())
rhombus(num)
