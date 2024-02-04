friends_list = input().split(", ")
blacklisted_counter = 0
lost_counter = 0

while True:
    command = input().split()

    if command[0] == "Blacklist":
        name = command[1]
        index = 0

        if name in friends_list:
            index = int(friends_list.index(name))
            friends_list[index] = "Blacklisted"
            blacklisted_counter += 1
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")

    elif command[0] == "Error":
        index = int(command[1])
        name = ""

        if 0 <= index < len(friends_list):
            name = friends_list[index]
            if name != "Blacklisted" and name != "Lost":
                friends_list[index] = "Lost"
                lost_counter += 1
                print(f"{name} was lost due to an error.")
            else:
                continue

    elif command[0] == "Change":
        index = int(command[1])
        name = ""
        new_name = command[2]

        if 0 <= index < len(friends_list):
            name = friends_list[index]
            friends_list[index] = new_name
            print(f"{name} changed his username to {new_name}.")

    elif command[0] == "Report":
        print(f"Blacklisted names: {blacklisted_counter}")
        print(f"Lost names: {lost_counter}")
        print(*friends_list, sep=" ")
        break
