force = {}

while True:
    command = input()
    if command == "Lumpawaroo"
        break

    if " | " in command:
        force_side, force_user = command.split(" | ")

        if force_side and force_user not in force:
            force[force_side] = force_user
        elif force_user not in force:
            force[force_side] = force_user
        elif force_user in force:
            continue

    elif " -> " in command:
        force_side, force_user = command.split(" -> ")

        if force_user in force:
            










