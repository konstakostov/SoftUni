from collections import deque

num = int(input())
num_stack = deque()

for _ in range(num):
    query = input().split()

    if query[0] == "1":
        num_stack.append(query[1])
    elif query[0] == "2" and num_stack:
        num_stack.pop()
    elif query[0] == "3" and num_stack:
        print(max(num_stack))
    elif query[0] == "4" and num_stack:
        print(min(num_stack))

num_stack.reverse()

print(*num_stack, sep=", ")
