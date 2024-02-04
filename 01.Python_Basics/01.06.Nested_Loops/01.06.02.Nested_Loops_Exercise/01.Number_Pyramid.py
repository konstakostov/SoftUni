num = int(input())

current = 1

current_bigger_num = False

for rows in range(1, num + 1):
    for cols in range(1, rows + 1):

        if current > num:
            current_bigger_num = True
            break

        print(str(current) + " ", end="")

        current += 1

    if current_bigger_num:
        break

    print()
