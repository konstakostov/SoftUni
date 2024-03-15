gifts = input().split(" ")

commands_list = []

while True:
    command_input = input()

    if command_input == "No Money":
        break
    else:
        commands_list.append(command_input.split(" "))

    for command in commands_list:
        if command[0] == "OutOfStock":
            for gift in gifts:
                if gift == command[1]:
                    gifts.remove(command[1])

        # elif command[0] == "Required":
        #
        #     position = int(command[-1])
        #
        #     for gift in gifts:
        #         gift[position] = command[2]

        elif command[0] == "JustInCase":
            for gift in gifts:
                if enumerate(gift) == command[-1]:
                    gift = command[1]

    commands_list = []

print(gifts)


