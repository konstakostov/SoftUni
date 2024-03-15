size = int(input())

matrix = []

for _ in range(size):
    # matrix.append(list(input()))
    current_row = list(input())
    matrix.append(current_row)

symbol = input()
position = None

for row in range(size):
    if position:
        break
    for col in range(size):
        if symbol == matrix[row][col]:
            position = (row, col)
            break

if position:
    print(position)
else:
    print(f"{symbol} does not occur in the matrix")
