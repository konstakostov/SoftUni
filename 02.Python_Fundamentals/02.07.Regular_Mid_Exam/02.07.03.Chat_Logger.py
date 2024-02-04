chat = []

while True:
    command = input()
    if command == "end":
        break

    if command.split()[0] == "Chat":
        message = command.split()[1]
        chat.append(message)

    elif command.split()[0] == "Delete":
        message = command.split()[1]
        for text in chat:
            if message == text:
                chat.remove(message)

    elif command.split()[0] == "Edit":
        message = command.split()[1]
        message_edited = command.split()[2]
        for text in chat:
            if message == text:
                message_index = chat.index(message)
                chat[message_index] = message_edited

    elif command.split()[0] == "Pin":
        message = command.split()[1]
        for text in chat:
            if message == text:
                message_index = chat.index(text)
                chat.remove(message)
                chat.append(message)

    elif command.split()[0] == "Spam":
        spam = command.split()
        spam.pop(0)

        for spam_message in spam:
            chat.append(spam_message)

print("\n".join(chat))
