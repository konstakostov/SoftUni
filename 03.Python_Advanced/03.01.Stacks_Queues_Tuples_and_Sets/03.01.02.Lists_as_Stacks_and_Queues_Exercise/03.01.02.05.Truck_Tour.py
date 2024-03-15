from collections import deque

pumps = int(input())
data = deque([[int(x) for x in input().split()] for _ in range(pumps)])

data_copy = data.copy()
gas = 0
index = 0

while data_copy:
    petrol, distance = data_copy.popleft()
    gas += petrol

    if gas >= distance:
        gas -= distance
    else:
        data.rotate(-1)
        data_copy = data.copy()
        index += 1
        gas = 0

print(index)
