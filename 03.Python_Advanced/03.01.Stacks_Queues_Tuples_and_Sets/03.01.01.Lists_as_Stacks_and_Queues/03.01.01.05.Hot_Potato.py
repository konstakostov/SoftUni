from collections import deque

kids = deque(input().split())
n_toss = int(input()) - 1

while len(kids) > 1:
    kids.rotate(-n_toss)
    kid_removed = kids.popleft()
    print(f"Removed {kid_removed}")

print(f"Last is {kids.popleft()}")
