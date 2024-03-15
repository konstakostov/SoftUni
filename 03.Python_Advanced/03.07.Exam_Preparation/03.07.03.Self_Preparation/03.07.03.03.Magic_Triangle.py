def get_magic_triangle(num):
    matrix = []

    index = 0

    for row in range(1, num + 1):
        elem = []

        for col in range(1, row + 1):
            if col == 1 or col == row:
                elem.append(1)
            else:
                above_sum = matrix[row - 2][index] + matrix[row - 2][index + 1]
                elem.append(above_sum)
                index += 1

        matrix.append(elem)
        index = 0

    return matrix


get_magic_triangle(5)
