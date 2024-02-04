n = int(input())

for i in range(n):
    line = input()

    string_pure = True

    for ch in line:
        if ch == "," or ch == "." or ch == "_":
            string_pure = False

    if string_pure:
        print(f"{line} is pure.")
    else:
        print(f"{line} is not pure!")
