size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

primary_sum = sum([matrix[i][i] for i in range(size)])
secondary_sum = sum([matrix[i][(size - 1) - i] for i in range(size)])

print(abs(primary_sum - secondary_sum))
