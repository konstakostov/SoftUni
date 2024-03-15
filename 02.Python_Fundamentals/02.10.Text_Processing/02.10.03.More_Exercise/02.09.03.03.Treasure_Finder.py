key = input().split()
command = input()

while command != "find":
    text = ""
    index = 0
    for char in command:
        text += chr(ord(char) - int(key[index]))
        index += 1
        if index == len(key):
            index = 0

    treasure_start = text.find("&")
    treasure_end = text.find("&", treasure_start + 1)
    treasure = text[treasure_start + 1: treasure_end]
    coordinates = text[text.find("<") + 1: text.find(">")]

    print(f"Found {treasure} at {coordinates}")

    command = input()
