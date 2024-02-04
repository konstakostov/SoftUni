lines = int(input())

capacity = 255
filled = 0

for i in range(lines):
    line = int(input())

    if capacity < (filled + line):
        print("Insufficient capacity!")
    else:
        filled += line

print(filled)
