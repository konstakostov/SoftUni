divisor = int(input())
boundary = int(input())

num = 0
max_num = 0

for i in range(1, boundary + 1):
    if i % divisor == 0:
        num = i

    if boundary >= num > 0:
        max_num = num

print(max_num)
