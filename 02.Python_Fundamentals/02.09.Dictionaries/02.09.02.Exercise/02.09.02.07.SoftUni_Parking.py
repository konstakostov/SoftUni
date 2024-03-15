num_commands = int(input())
parking = {}

for i in range(num_commands):
    command = input()

    if command.split()[0] == "register":
        username = command.split()[1]
        license_plate = command.split()[2]

        if username not in parking:
            parking[username] = license_plate
            print(f"{username} registered {parking[username]} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking[username]}")

    elif command.split()[0] == "unregister":
        username = command.split()[1]

        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")

for username, license_plate in parking.items():
    print(f"{username} => {license_plate}")
