rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

square_matrix = []
square_sum = float('-inf')

for row in range(rows - 2):
    for col in range(columns - 2):
        first_row = matrix[row][col:col+3]
        second_row = matrix[row+1][col:col+3]
        third_row = matrix[row+2][col:col+3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if square_sum < current_sum:
            square_sum = current_sum
            square_matrix = [first_row, second_row, third_row]

print(f"Sum = {square_sum}")
[print(*row) for row in square_matrix]
