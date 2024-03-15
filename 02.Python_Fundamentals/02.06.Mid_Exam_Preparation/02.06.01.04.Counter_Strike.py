energy = int(input())
battles = 0

status = True

while True:
    command = input()

    if command == "End of battle":
        break

    distance = int(command)

    if energy - distance >= 0:
        battles += 1
        energy -= distance
    else:
        status = False
        break

    if battles % 3 == 0:
        energy += battles

if status:
    print(f"Won battles: {battles}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {battles} won battles and {energy} energy")
