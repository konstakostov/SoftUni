import sys

n = int(input())

max_num = -sys.maxsize
num_sum = 0

for _ in range(n):
    num = int(input())

    if num > max_num:
        max_num = num

    num_sum += num

if max_num == num_sum - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {abs(max_num - (num_sum - max_num))}")
