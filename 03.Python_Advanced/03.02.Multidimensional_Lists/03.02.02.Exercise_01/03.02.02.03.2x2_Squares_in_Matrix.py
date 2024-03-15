rows, columns = [int(x) for x in input().split()]

matrix = []
square_matrix = 0

for _ in range(rows):
    matrix.append([x for x in input().split()])

for row in range(rows - 1):
    for col in range(columns - 1):
        current = matrix[row][col]
        right = matrix[row][col + 1]
        bottom = matrix[row + 1][col]
        diagonal = matrix[row + 1][col + 1]

        if current == right == bottom == diagonal:
            square_matrix += 1

print(square_matrix)
