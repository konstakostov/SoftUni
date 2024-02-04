trunk_capacity = float(input())

filled_space = 0

suitcases_loaded = 0

while filled_space < trunk_capacity:
    command = input()

    if command == "End":
        print(f"Congratulations! All suitcases are loaded!")
        break

    suitcase = float(command)

    if (filled_space + suitcase) < trunk_capacity:
        filled_space += suitcase
        suitcases_loaded += 1
    else:
        print(f"No more space!")
        break

print(f"Statistic: {suitcases_loaded} suitcases loaded.")

























# volume_capacity = float(input())
#
# volume_filled = 0
#
# suitcases_count = 0
#
# while volume_filled <= volume_capacity:
#     command = input()
#
#     if command == "End":
#         print(f"Congratulations! All suitcases are loaded!")
#         print(f"Statistic: {suitcases_count} suitcases loaded.")
#         break
#
#     suitcase_volume = float(command)
#     suitcases_count += 1
#
#     if suitcases_count % 3 == 0:
#         suitcase_volume *= 0.90
#
#     volume_filled += suitcase_volume
#
# else:
#     suitcases_count -= 1
#     print(f"No more space!")
#     print(f"Statistic: {suitcases_count} suitcases loaded.")

