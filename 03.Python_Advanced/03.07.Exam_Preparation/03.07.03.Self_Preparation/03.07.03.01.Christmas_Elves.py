from collections import deque

energy = deque([int(x) for x in input().split()])
boxes = deque([int(x) for x in input().split()])

toys = 0
energy_used = 0

COOKIE = 1
CHOCOLATE = 2

counter = 1

while energy and boxes:
    elf = energy.popleft()
    if elf < 5:
        counter += 1
        continue

    box = boxes.pop()

    if elf >= box:
        if counter % 3 == 0 and counter % 5 == 0:
            if elf >= box * 2:
                elf -= box * 2
                energy.append(elf)  # Eats 04.03.01.01.Food cookie and back of line

                energy_used += box * 2

        elif counter % 5 == 0:
            elf -= box
            energy.append(elf)  # Doesn't get cookie and back of line

            energy_used += box

        elif counter % 3 == 0:
            if elf >= box * 2:
                elf -= box * 2
                energy.append(elf + 1)  # Eats 04.03.01.01.Food cookie and back of line

                energy_used += box * 2
                toys += 2
            else:
                energy.append(elf * 2)
                boxes.append(box)

        else:
            elf -= box
            energy.append(elf + 1)  # Eats 04.03.01.01.Food cookie and back of line

            energy_used += box
            toys += 1

    else:
        energy.append(elf * 2)  # Gets hot choco and back of line
        boxes.append(box)

    counter += 1


print(f"Toys: {toys}")
print(f"Energy: {energy_used}")

if energy:
    print(f"Elves left: {', '.join([str(x) for x in energy])}")
if boxes:
    print(f"Boxes  left: {', '.join([str(x) for x in boxes])}")
