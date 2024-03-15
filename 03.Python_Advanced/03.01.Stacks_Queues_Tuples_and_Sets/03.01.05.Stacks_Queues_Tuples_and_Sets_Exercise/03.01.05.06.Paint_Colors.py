from collections import deque

substrings = deque(x for x in input().split())

formed = []
colors = {'red', 'yellow', 'blue', 'orange', 'purple', 'green'}
secondary = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'}
}

while substrings:
    first = substrings.popleft()
    second = substrings.pop() if substrings else ""

    for color in (first + second, second + first):
        if color in colors:
            formed.append(color)
            break
    for el in first[:-1], second[:-1]:
        substrings.insert(len(substrings) // 2, el)

for f_color in set(secondary.keys()).intersection(formed):
    if not secondary[f_color].issubset(formed):
        formed.remove(f_color)

print(formed)

# from collections import deque
#
# substrings = deque(x for x in input().split())
#
# collected = []
#
# colors = {'red', 'yellow', 'blue', 'orange', 'purple', 'green'}
# secondary_colors = {
#     'orange': {'red', 'yellow'},
#     'purple': {'red', 'blue'},
#     'green': {'yellow', 'blue'}
# }
#
# while substrings:
#     first = substrings.popleft()
#     second = substrings.pop() if substrings else ""
#
#     for color in {first + second, second + first}:
#         if color in colors:
#             collected.append(color)
#             break
#     else:
#         for elem in first[:-1], second[:-1]:
#             if elem:
#                 substrings.insert(len(substrings) // 2, elem)
#
# for color in set(secondary_colors.keys()).intersection(collected):
#     if not secondary_colors[color].issubset(collected):
#         collected.remove(color)
#
# print(collected)
