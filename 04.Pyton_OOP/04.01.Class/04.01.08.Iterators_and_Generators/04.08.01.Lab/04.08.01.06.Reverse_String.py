def reverse_text(text: str):
    current = len(text) - 1
    end = 0

    while current >= end:
        yield text[current]

        current -= 1


for char in reverse_text("step"):
    print(char, end='')
