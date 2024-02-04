odd = set()
even = set()

for row in range(1, int(input()) + 1):
    name_sum = sum(ord(char) for char in input()) // row

    if name_sum % 2 == 0:
        even.add(name_sum)
    else:
        odd.add(name_sum)


if sum(odd) == sum(even):
    print(*odd.union(even), sep=', ')
elif sum(odd) > sum(even):
    print(*odd.difference(even), sep=', ')
elif sum(odd) < sum(even):
    print(*even.symmetric_difference(odd), sep=', ')
