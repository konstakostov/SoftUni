message = input()

encrypted_message = ""

for char in message:
    encrypted_char = ord(char) + 3
    encrypted_message += chr(encrypted_char)

print(encrypted_message)
