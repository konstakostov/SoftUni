# # 01. Sum Matrix Elements, Variant 01
# rows, cols = [int(el) for el in input().split(', ')]
#
# matrix = []
# matrix_sum = 0
#
# for _ in range(rows):
#     inner_list = [int(el) for el in input().split(', ')]
#     matrix.append(inner_list)
#
# for row_index in range(rows):
#     for col_index in range(cols):
#         matrix_sum += int(matrix[row_index][col_index])
#
# print(matrix_sum)
# print(matrix)
#
#
# # 01. Sum Matrix Elements, Variant 02
# rows, cols = [int(el) for el in input().split(', ')]
#
# matrix = []
# matrix_sum = 0
#
# for _ in range(rows):
#     inner_list = [int(el) for el in input().split(', ')]
#     matrix_sum += sum(inner_list)
#     matrix.append(inner_list)
#
# print(matrix_sum)
# print(matrix)
#
#
#
# # 02. Even Matrix, Version 01
# rows = int(input())
#
# matrix = []
#
# for row_index in range(rows):
#     inner_list = [int(el) for el in input().split(', ') if int(el) % 2 == 0]
#     matrix.append(inner_list)
#
# print(matrix)
#
#
# # 02. Even Matrix, Version 02
# rows = int(input())
#
# matrix = [[int(el) for el in input().split(', ') if int(el) % 2 == 0]
#           for row_index in range(rows)]
#
# print(matrix)
#
#
# # 02. Even Matrix, Version 03
# print([[int(el) for el in input().split(', ') if int(el) % 2 == 0]
#        for row_index in range(int(input()))])
#
#
#
# # 03. Flattening Matrix
# row = int(input())
#
# flatten = []
#
# for _ in range(row):
#     inner_list = [int(el) for el in input().split(', ')]
#     flatten.extend(inner_list)
#
# print(flatten)
#
#
#
# # 04. Sum Matrix Columns
# rows, columns = [int(el) for el in input().split(', ')]
#
# matrix = []
#
# for row_index in range(rows):
#     inner_list = [int(el) for el in input().split()]
#     matrix.append(inner_list)
#
# column_sums = []
#
# for col_index in range(columns):
#     sum_col = 0
#     for row_index in range(rows):
#         sum_col += matrix[row_index][col_index]
#     column_sums.append(sum_col)
#
# for column_sum in column_sums:
#     print(column_sum)
#
#
#
# # 05. Primary Diagonal
# rows = int(input())
#
# matrix = []
#
# for _ in range(rows):
#     inner_list = [int(el) for el in input().split()]
#     matrix.append(inner_list)
#
# diagonal_sum = 0
#
# for index in range(rows):
#     diagonal_sum += matrix[index][index]
#
# print(diagonal_sum)
#
#
#
# # 06. Symbol in Matrix
# rows = int(input())
#
# matrix = []
#
# for _ in range(rows):
#     inner_list = list(input())
#     matrix.append(inner_list)
#
# symbol = input()
# position = None
#
# for row in range(rows):
#     if position:
#         break
#     for col in range(rows):
#         if symbol == matrix[row][col]:
#             position = (row, col)
#             break
#
# if position:
#     print(position)
# else:
#     print(f"{symbol} does not occur in the matrix")
#
#
#
# # 07. Square with Maximum SUm
# rows, columns = [int(x) for x in input().split(', ')]
#
# matrix = []
#
# for _ in range(rows):
#     inner_list = [int(el) for el in input().split(', ')]
#     matrix.append(inner_list)
#
# max_sum = float('-inf')
# sub_matrix = []
#
# for row_index in range(rows - 1):
#     for col_index in range(columns - 1):
#         current_element = matrix[row_index][col_index]
#         element_below = matrix[row_index + 1][col_index]
#         element_next = matrix[row_index][col_index + 1]
#         element_diagonal = matrix[row_index + 1][col_index + 1]
#
#         sum_elements = current_element + element_below + element_next + element_diagonal
#
#         if max_sum < sum_elements:
#             max_sum = sum_elements
#             sub_matrix = [[current_element, element_next], [element_below, element_diagonal]]
#
# print(*sub_matrix[0], sep=' ')
# print(*sub_matrix[1], sep=' ')
# print(max_sum)
#
#
