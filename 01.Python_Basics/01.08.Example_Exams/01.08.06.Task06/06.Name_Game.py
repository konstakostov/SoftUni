max_points = 0
max_name = ""

while True:
    name = input()

    if name == "Stop":
        print(f"The winner is {max_name} with {max_points} points!")
        break

    points = 0

    for i in range(0, len(name)):
        num = int(input())

        if num == ord(name[i]):
            points += 10
        else:
            points += 2

    if points >= max_points:
        max_points = points
        max_name = name

