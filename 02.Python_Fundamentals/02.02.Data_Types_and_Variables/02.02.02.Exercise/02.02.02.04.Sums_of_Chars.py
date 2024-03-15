entries = int(input())

char_sum = 0

for i in range(entries):
    char = input()

    char_sum += ord(char)

print(f"The sum equals: {char_sum}")
