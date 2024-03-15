rows, columns = [int(x) for x in input().split(', ')]

matrix = []
column_sums = []

for _ in range(rows):
    current_row = [int(x) for x in input().split()]
    matrix.append(current_row)

for col in range(columns):
    sum_col = 0

    for row in range(rows):
        sum_col += matrix[row][col]

    column_sums.append(sum_col)

print(*column_sums, sep='\n')
