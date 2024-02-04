def reverse_text(text: str):
    index = len(text) - 1
    end = 0

    while index >= end:
        yield text[index]

        index -= 1


for char in reverse_text("step"):
    print(char, end='')
