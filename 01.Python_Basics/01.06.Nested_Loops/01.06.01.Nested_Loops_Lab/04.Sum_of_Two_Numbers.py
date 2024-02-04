# start = int(input())
# end = int(input())
# magic_n = int(input())
#
# counter = 0
#
# num_found = False
#
# for x1 in range(start, end + 1):
#     if num_found:
#         break
#
#     for x2 in range(start, end + 1):
#         counter += 1
#         if x1 + x2 == magic_n:
#             print(f"Combination N:{counter} ({x1} + {x2} = {magic_n})")
#             num_found = True
#             break
#
# if not num_found:
#     print(f"{counter} combinations - neither equals {magic_n}")

start = int(input())
end = int(input())
magic_n = int(input())

counter = 0

found_num = False

for x1 in range(start, end + 1):
    if found_num:
        break

    for x2 in range(start, end + 1):
        counter += 1
        if x1 + x2 == magic_n:
            print(f"Combination N:{counter} ({x1} + {x2} = {magic_n})")
            found_num = True
            break

if not found_num:
    print(f"{counter} combinations - neither equals {magic_n}")
