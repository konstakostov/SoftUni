# # 01. CLOCK
# for h in range(24):
#     for m in range(60):
#         print(f"{h}:{m}")
#


# # 02. MULTIPLICATION TABLE
# for x1 in range(1, 11):
#     for x2 in range(1, 11):
#         x = x1 * x2
#         print(f"{x1} * {x2} = {x}")
#


# 03. COMBINATIONS
n = int(input())

counter = 0

for x1 in range(n + 1):
    for x2 in range(n + 1):
        for x3 in range(n + 1):

            if (x1 + x2 + x3) == n:
                counter += 1
                print(f"Counter: {counter} \n"
                      f"Numbers: {x1} {x2} {x3}")
print(counter)


