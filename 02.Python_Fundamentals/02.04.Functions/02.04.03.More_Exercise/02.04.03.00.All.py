# # 01. Data Types
# def data_type(user_type, user_input):
#     result = None
#
#     if user_type == "int":
#         result = int(user_input) * 2
#     elif user_type == "real":
#         result = (float(user_input) * 1.5)
#     elif user_type == "string":
#         result = f"${user_input}$"
#
#     return result
#
#
# type_input = input()
# num_input = input()
#
# final_result = data_type(type_input, num_input)
#
# if type_input == "real":
#     print(f"{final_result:.2f}")
# else:
#     print(final_result)
#


# 02. Center Point
import math


def cartesian(x1, y1, x2, y2):
    if x1 < x2 or y1 < y2:
        result = f"({x1}, {y1})"
    elif x1 == x2 or y1 == y2:
        result = f"({x1}, {y1})"
    else:
        result = f"({x2}, {y2})"

    return result


x_1 = math.floor(float(input()))
y_1 = math.floor(float(input()))
x_2 = math.floor(float(input()))
y_2 = math.floor(float(input()))

coordinates = cartesian(x_1, y_1, x_2, y_2)

print(coordinates)
