size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

while True:
    command, *data = input().split()

    if command == "END":
        [print(*r) for r in matrix]
        break
    else:
        row, column, value = int(data[0]), int(data[1]), int(data[2])

    if 0 <= row < size and 0 <= column < size:
        if command == "Add":
            matrix[row][column] += value
        elif command == "Subtract":
            matrix[row][column] -= value
    else:
        print("Invalid coordinates")
