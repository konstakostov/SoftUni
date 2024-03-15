size = int(input())

matrix = []
diagonal_sum = 0

for _ in range(size):
    current_row = [int(x) for x in input().split()]
    matrix.append(current_row)

for index in range(size):
    diagonal_sum += matrix[index][index]

print(diagonal_sum)
