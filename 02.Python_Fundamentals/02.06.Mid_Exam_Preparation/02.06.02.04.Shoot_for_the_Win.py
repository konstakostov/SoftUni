target_list = list(map(int, input().split()))
forbidden_indexes = [0] * len(target_list)

new_target_values = []
target_counter = 0
old_value = 0

while True:
    command = input()

    if command == "End":
        break

    index = int(command)

    if index > len(target_list) - 1 or forbidden_indexes[index] == 1:
        continue
    else:
        old_value = target_list[index]
        target_list[index] = -1
        forbidden_indexes[index] = 1
        target_counter += 1

        new_target_values = []

        for target in target_list:
            if target > old_value and target != -1:
                target -= old_value
                new_target_values.append(target)
            elif target <= old_value and target != -1:
                target += int(old_value)
                new_target_values.append(target)
            else:
                new_target_values.append(target)

    target_list = new_target_values

target_list = map(str, target_list)

print(f"Shot targets: {target_counter} -> {' '.join(target_list)}")
