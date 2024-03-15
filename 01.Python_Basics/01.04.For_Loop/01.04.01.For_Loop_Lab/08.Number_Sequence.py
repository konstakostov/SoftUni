import sys

n = int(input())

max_n = -sys.maxsize
min_n = sys.maxsize

for i in range(0, n):
    num = int(input())
    if i == 0:
        max_n = num
        min_n = num
    else:
        if num > max_n:
            max_n = num
        elif num < min_n:
            min_n = num

print(f"Max number: {max_n}")
print(f"Min number: {min_n}")
