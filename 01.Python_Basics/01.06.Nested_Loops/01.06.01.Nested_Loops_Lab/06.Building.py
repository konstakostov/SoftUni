floors = int(input())
rooms = int(input())

for i in range(floors, 0, -1):
    for j in  range(rooms):
        if i == floors:
            print(f"L{i}{j}", end=" ")
            continue
        elif i % 2 != 0:
            print(f"A{i}{j}", end=" ")
            continue
        else:
            print(f"O{i}{j}", end=" ")
            continue
    print(f"")
