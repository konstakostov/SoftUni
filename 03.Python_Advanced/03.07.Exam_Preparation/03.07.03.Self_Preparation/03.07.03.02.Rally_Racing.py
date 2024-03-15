size = int(input())
car_number = input()

car_route = []
distance = 0
finish = False

car_pos = [0, 0]

tunnel_01_pos = []
tunnel_02_pos = []


for row in range(size):
    car_route.append(input().split())

    if "T" in car_route[row]:
        if not tunnel_01_pos:
            tunnel_01_pos = [row, car_route[row].index("T")]
        else:
            tunnel_02_pos = [row, car_route[row].index("T")]


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


while True:
    command = input()
    if command == "End":
        car_route[car_pos[0]][car_pos[1]] = "C"
        break

    r = car_pos[0] + directions[command][0]
    c = car_pos[1] + directions[command][1]

    if not (0 <= r < size and 0 <= c < size):
        break

    if car_route[r][c] == ".":
        distance += 10
        car_pos = [r, c]

    if car_route[r][c] == "T":
        if [r, c] == tunnel_01_pos:
            car_pos = tunnel_02_pos

            car_route[tunnel_01_pos[0]][tunnel_01_pos[1]] = "."
            car_route[tunnel_02_pos[0]][tunnel_02_pos[1]] = "."

        elif c[r, c] == tunnel_02_pos:
            car_pos = tunnel_01_pos

            car_route[tunnel_01_pos[0]][tunnel_01_pos[1]] = "."
            car_route[tunnel_02_pos[0]][tunnel_02_pos[1]] = "."

        distance += 30

    if car_route[r][c] == "F":
        distance += 10
        car_pos = [r, c]

        car_route[r][c] = "C"
        finish = True

        break

if finish:
    print(f"Racing car {car_number} finished the stage!")
else:
    print(f"Racing car {car_number} DNF.")

print(f"Distance covered {distance} km.")

print(*[''.join(row) for row in car_route], sep="\n")
