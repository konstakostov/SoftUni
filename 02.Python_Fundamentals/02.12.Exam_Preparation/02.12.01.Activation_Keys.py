key = input()

while True:
    command = input()
    if command == "Generate":
        print(f"Your activation key is: {key}")
        exit(0)

    instructions = command.split(">>>")

    if instructions[0] == "Contains":
        substring = instructions[1]

        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print("Substring not found!")

    elif instructions[0] == "Flip":
        case = instructions[1]
        start_index = int(instructions[2])
        end_index = int(instructions[3])
        changed_string = ""

        if case == "Upper":
            changed_string = key[start_index:end_index].upper()
        elif case == "Lower":
            changed_string = key[start_index:end_index].lower()

        key = key[:start_index] + changed_string + key[end_index::]
        print(key)

    elif instructions[0] == "Slice":
        start_index = int(instructions[1])
        end_index = int(instructions[2])

        key = key[:start_index] + key[end_index::]
        print(key)
