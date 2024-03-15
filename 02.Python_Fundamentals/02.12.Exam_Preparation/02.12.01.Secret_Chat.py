message = input()

while True:
    command = input()
    if command == "Reveal":
        break

    action = command.split(":|:")[0]

    if action == "InsertSpace":
        index = int(command.split(":|:")[1])

        message = message[:index] + " " + message[index::]

    elif action == "Reverse":
        substring = command.split(":|:")[1]

        if substring in message:
            message = message.replace(substring, "", 1) + substring[::-1]
        else:
            print("error")
            continue

    elif action == "ChangeAll":
        substring = command.split(":|:")[1]
        replacement = command.split(":|:")[2]

        if substring in message:
            message = message.replace(substring, replacement)

    print(message)

print(f"You have a new text message: {message}")
