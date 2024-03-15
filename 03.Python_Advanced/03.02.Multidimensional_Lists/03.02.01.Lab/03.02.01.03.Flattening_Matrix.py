rows = int(input())

flat_matrix = []

for _ in range(rows):
    current_row = [int(x) for x in input().split(', ')]
    flat_matrix += current_row

print(flat_matrix)
