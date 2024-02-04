row, col = [int(x) for x in input().split(', ')]

matrix = []
matrix_sum = 0


for r in range(row):
    elem = [int(x) for x in input().split(', ')]
    matrix.append(elem)
    matrix_sum += sum(elem)

print(matrix_sum)
print(matrix)
