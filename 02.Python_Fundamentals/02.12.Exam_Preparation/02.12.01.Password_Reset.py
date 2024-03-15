password = input()

while True:
    command = input()
    if command == "Done":
        print(f"Your password is: {password}")
        exit(1)

    if command == "TakeOdd":
        temp_password = ""
        for i in range(len(password)):
            if i % 2 != 0:
                temp_password += password[i]
        password = temp_password
        temp_password = ""

    elif command.split(" ")[0] == "Cut":
        index = int(command.split(" ")[1])
        length = int(command.split(" ")[2])
        substring = ""

        for i in range(index, index + length):
            substring += password[i]
        password = password.replace(substring, "", 1)
        temp_password = ""

    elif command.split(" ")[0] == "Substitute":
        substring = command.split(" ")[1]
        substitute = command.split(" ")[2]
        if substring in password:
            password = password.replace(substring, substitute)
        else:
            print("Nothing to replace!")
            continue

    print(password)
