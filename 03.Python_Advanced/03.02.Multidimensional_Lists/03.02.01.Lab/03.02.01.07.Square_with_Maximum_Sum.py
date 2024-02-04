rows, columns = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

sub_matrix = []
max_sum = float('-inf')

for row in range(rows - 1):
    for col in range(columns - 1):
        current = matrix[row][col]
        right = matrix[row][col + 1]
        bottom = matrix[row + 1][col]
        diagonal = matrix[row + 1][col + 1]

        sum_elements = current + right + bottom + diagonal

        if max_sum < sum_elements:
            max_sum = sum_elements
            sub_matrix = [[current, right], [bottom, diagonal]]

print(*sub_matrix[0], sep=' ')
print(*sub_matrix[1], sep=' ')
print(max_sum)
