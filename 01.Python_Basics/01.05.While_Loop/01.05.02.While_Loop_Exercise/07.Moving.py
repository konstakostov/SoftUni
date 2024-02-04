flat_volume = int(input()) * int(input()) * int(input())
box_volume = 1

while flat_volume > 0:
    command = input()

    if command == "Done":
        print(f"{flat_volume} Cubic meters left.")
        break

    boxes = int(command)
    boxes_volume = boxes * box_volume
    flat_volume -= boxes_volume

if flat_volume <= 0:
    print(f"No more free space! You need {abs(flat_volume)} Cubic meters more.")
