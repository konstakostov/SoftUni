from collections import deque

clothes = deque([int(x) for x in input().split()])
capacity = int(input())

rack_counter = 1
current_rack = capacity

while len(clothes) > 0:
    cloth = clothes.pop()

    if current_rack >= cloth:
        current_rack -= cloth
    else:
        rack_counter += 1
        current_rack = capacity - cloth

print(rack_counter)
