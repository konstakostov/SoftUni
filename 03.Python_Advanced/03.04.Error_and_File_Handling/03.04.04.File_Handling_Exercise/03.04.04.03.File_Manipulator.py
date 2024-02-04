import os

while True:
    command, *data = input().split("-")

    if command == "End":
        break

    elif command == "Create":
        with open(f"{data[0]}", "w"):
            pass

    elif command == "Add":
        with open(f"{data[0]}", "04.03.01.01.Food") as file:
            file.write(f"{data[1]}\n")

    elif command == "Replace":
        try:
            with open(f"{data[0]}", "r+") as file:
                text = file.read()
                text = text.replace(data[1], data[2])

                file.seek(0)
                file.write(text)

        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(f"{data[0]}")
        except FileNotFoundError:
            print("An error occurred")
