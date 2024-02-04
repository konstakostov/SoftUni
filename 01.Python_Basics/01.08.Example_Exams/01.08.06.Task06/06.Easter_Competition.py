breads_num = int(input())

points = 0

max_points = 0
max_points_baker = ""

for i in range(breads_num):
    baker = input()
    while True:
        command = input()

        if command == "Stop":
            print(f"{baker} has {points} points.")
            if points > max_points:
                max_points = points
                max_points_baker = baker
                print(f"{max_points_baker} is the new number 1!")
            points = 0
            break

        grade = int(command)
        points += grade

print(f"{max_points_baker} won competition with {max_points} points!")
