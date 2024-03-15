array_input = list(map(int, input().split()))

while True:
    command = input()

    if command == "end":
        break
    elif command == "decrease":
        for index in range(len(array_input)):
            array_input[index] -= 1
    else:
        action, index_01, index_02 = command.split()
        index_01 = int(index_01)
        index_02 = int(index_02)

        if action == "swap":
            array_input[index_01], array_input[index_02] = array_input[index_02], array_input[index_01]
        elif action == "multiply":
            array_input[index_01] = array_input[index_01] * array_input[index_02]

print(*array_input, sep=", ")
