# # 01. Reverse Number
# from collections import deque
#
# stack = deque(input().split())
#
# for i in range(len(stack)):
#     print(stack.pop(), end=" ")
#


# # 02. Stacked Queries
# from collections import deque
#
# stack = deque()
#
# for i in range(int(input())):
#     query = [int(x) for x in input().split()]
#     command = query[0]
#
#     if command == 1:
#         stack.append(query[1])
#
#     elif command == 2:
#         if stack:
#             stack.pop()
#
#     elif command == 3:
#         if stack:
#             print(max(stack))
#
#     elif command == 4:
#         if stack:
#             print(min(stack))
#
# stack.reverse()
# print(*stack, sep=", ")
#


# # 03. Fast Food
# from collections import deque
#
# daily_food = int(input())
# orders = deque(int(x) for x in input().split())
# orders_copy = orders.copy()
#
# print(max(orders))
#
# while len(orders) > 0:
#     current = orders_copy.popleft()
#
#     if daily_food >= current:
#         daily_food -= current
#         orders.popleft()
#     else:
#         break
#
# if not orders:
#     print("Orders complete")
# else:
#     print(f"Orders left: {' '.join([str(x) for x in orders])}")
#


# # 04. Fashion Boutique
# from collections import deque
#
# clothes = deque([int(x) for x in input().split()])
# rack_capacity = int(input())
#
# current_capacity = rack_capacity
# racks_count = 1
#
# while clothes:
#     clothing = clothes.pop()
#
#     if current_capacity >= clothing:
#         current_capacity -= clothing
#     else:
#         racks_count += 1
#         current_capacity = rack_capacity
#         current_capacity -= clothing
#
# print(racks_count)
#


# 05. Truck Tour
# from collections import deque
#
# pumps = int(input())
# pumps_data = deque([int(x) for x in input().split()] for _ in range(pumps))
# pumps_data_copy = pumps_data.copy()
#
# gas_tank = 0
# index = 0
#
# while pumps_data_copy:
#     gas, distance = pumps_data_copy.popleft()
#
#     gas_tank += gas
#
#     if gas_tank >= distance:
#         gas_tank -= distance
#     else:
#         pumps_data.rotate(-1)
#         pumps_data_copy = pumps_data.copy()
#         gas_tank = 0
#         index += 1
#
# print(index)


# # 06. Balanced Parentheses
# from collections import deque
#
# parentheses = deque(list(input()))
# open_parentheses = deque()
#
# while parentheses:
#     current = parentheses.popleft()
#
#     if current in "([{":
#         open_parentheses.append(current)
#
#     elif not open_parentheses:
#         print("NO")
#         break
#
#     else:
#         parentheses_check = open_parentheses.pop() + current
#
#         if f"{parentheses_check}" not in "()[]{}":
#             print("NO")
#             break
# else:
#     print("YES")
#
