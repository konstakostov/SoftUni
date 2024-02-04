size = int(input())
matrix = [list(input()) for _ in range(size)]

positions = {
    (-2, 1),     # U-2, R-1
    (-1, 2),     # U-1, R-2
    (1, 2),     # D-1, R-2
    (2, 1),     # D-2, R-1
    (2, -1),     # D-2, L-1
    (1, -2),     # D-1, L-2
    (-1, -2),     # U-1, L-2
    (-2, -1),     # U-2, L-1
}

removed_knights = 0

while True:
    max_attacks = 0
    max_knight_position = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = 0

                for current_pos in positions:
                    pos_row = row + current_pos[0]
                    pos_col = col + current_pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1

                if max_attacks < attacks:
                    max_attacks = attacks
                    max_knight_position = [row, col]

    if max_knight_position:
        matrix[max_knight_position[0]][max_knight_position[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
