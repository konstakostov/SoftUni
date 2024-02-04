from collections import deque


def best_list_pureness(*args):
    num_list = deque(args[0])
    num = int(args[1])

    pureness = 0
    rotations = 0

    for i in range(0, num + 1):
        current = 0

        for j in range(len(num_list)):
            current += int(num_list[j]) * j

        if current > pureness:
            pureness = current
            rotations = 0 + i

        num_list.rotate(1)

    return f"Best pureness {pureness} after {rotations} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

print()

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

print()

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
