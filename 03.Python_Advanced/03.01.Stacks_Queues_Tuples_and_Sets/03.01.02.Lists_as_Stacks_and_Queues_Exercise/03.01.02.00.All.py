# # 01. Reverse Numbers, Version 01
# from collections import deque
#
# numbers = deque(input().split())
#
# for i in range(len(numbers)):
#     print(numbers.popleft(), end=" ")
#
#  # 01. Reverse Numbers, Version 01
# from collections import deque
#
# numbers = deque(input().split())
# numbers.reverse(),
#
# print(' '.join(numbers))
#


# # 02. Stacked Queries, Version 01
# from collections import deque
#
# numbers = deque()
#
# for _ in range(int(input())):
#     number_data = [int(x) for x in input().split()]
#     command = number_data[0]
#
#     if command == 1:
#         numbers.append(number_data[1])
#
#     elif command == 2:
#         if numbers:
#             numbers.pop()
#
#     elif command == 3:
#         if numbers:
#             print(max(numbers))
#
#     elif command == 4:
#         if numbers:
#             print(min(numbers))
#
# for _ in range(len(numbers)):
#     print(numbers.pop(), end=" ")
#
# # 02. Stacked Queries, Version 02
# from collections import deque
#
# numbers = deque()
#
# map_functions = {
#     1: lambda x: numbers.append(x[1]),  # x == number_data
#     2: lambda x: numbers.pop() if numbers else None,
#     3: lambda x: print(max(numbers)) if numbers else None,
#     4: lambda x: print(min(numbers)) if numbers else None
# }
#
# for _ in range(int(input())):
#     number_data = [int(x) for x in input().split()]
#     map_functions[number_data[0]](number_data)
#
# numbers.reverse()
#
# print(*numbers, sep=", ")
#


# # 03. Fast Food
# from collections import deque
#
# food = int(input())
#
# orders = deque([int(x) for x in input().split()])
#
# print(max(orders))
#
# for order in orders.copy():
#     if food >= order:
#         orders.popleft()
#         food -= order
#     else:
#         print(f"Orders left: {' '.join([str(x) for x in orders])}")
#         break
# else:
#     print("Orders complete")
#


# # 04. Fashion Boutique
# from collections import deque
#
# clothes = deque([int(x) for x in input().split()])
# rack_space = int(input())
#
# rack_count = 1
# current_rack_space = rack_space
#
# while clothes:
#     cloth = clothes.pop()
#
#     if current_rack_space >= cloth:
#         current_rack_space -= cloth
#     else:
#         rack_count += 1
#         current_rack_space = rack_space - cloth
#
# print(rack_count)
#


# # 05. Truck Tour
# from collections import deque
#
# pumps_data = [[int(x) for x in input().split()] for _ in range(int(input()))]
# # # Equivalent to the list comprehension
# # for i in range(int(input())):
# #     pumps_data[i] = []
# #     for x in input().split():
# #         pumps_data[i].append(int(x))
#
# pumps_data_copy = pumps_data.copy()
# gas_in_tank = 0
# index = 0
#
# while pumps_data_copy:
#     petrol, distance = pumps_data_copy.popleft()
#
#     gas_in_tank += petrol
#
#     if gas_in_tank >= distance:
#         gas_in_tank -= distance
#     else:
#         pumps_data.rotate(-1)
#         pumps_data_copy = pumps_data.copy()
#         index += 1
#         gas_in_tank = 0
#


# # 06. Balanced Parentheses
# from collections import deque
#
# parenthesis = deque(input())
# open_parenthesis = deque()
#
# while parenthesis:
#     current_parenthesis = parenthesis.popleft()
#
#     if current_parenthesis in "([{":
#         open_parenthesis.append(current_parenthesis)
#
#     elif not open_parenthesis:
#         print("NO")
#         break
#
#     else:
#         parenthesis_check = open_parenthesis.pop() + current_parenthesis
#         if f"{parenthesis_check}" not in "()[]{}":
#             print("NO")
#             break
# else:
#     print("YES")
#


# # 07. *Robotics
# from collections import deque
# from datetime import datetime, timedelta
#
# robots = {}
#
# for r in input().split(";"):
#     name, time_needed = r.split("-")
#     robots[name] = [int(time_needed), 0]
#
# factory_time = datetime.strptime(input(), '%H:%M:%S')
# products = deque()
#
# while True:
#     product = input()
#
#     if product == "End":
#         break
#
#     products.append(product)
#
# while products:
#     factory_time += timedelta(0, 1)
#     product = products.popleft()
#
#     free_robots = []
#
#     for name, value in robots.items():
#         if value[1] != 0:
#             robots[name][1] -= 1
#
#         if value[1] == 0:
#             free_robots.append([name, value])
#
#     if not free_robots:
#         products.append(product)
#         continue
#
#     robot_name, data = free_robots[0]
#     robots[robot_name][1] = data[0]
#
#     print(f"{robot_name} - {product} [{factory_time.strftime('%H:%M:%S')}]")
#


# 08. *Crossroads


# 09. *Key Revolver


# 10. *Cups and Bottles


