encrypted_message = input()

instructions = input()

while instructions != "Decode":
    command = instructions.split("|")

    if command[0] == "Move":
        index = int(command[1])

        first_part_message = encrypted_message[:index]
        second_part_message = encrypted_message[index::]
        encrypted_message = second_part_message + first_part_message

    elif command[0] == "Insert":
        index = int(command[1])
        value = str(command[2])

        encrypted_message = encrypted_message[:index] + value + encrypted_message[index::]

    elif command[0] == "ChangeAll":
        substring = str(command[1])
        replacement = str(command[2])

        encrypted_message = encrypted_message.replace(substring, replacement)

    instructions = input()

message = str(encrypted_message)
print(f"The decrypted message is: {message}")
