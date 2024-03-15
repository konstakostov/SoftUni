def office_chairs(rooms):
    free_chairs = 0
    needed_chairs = 0

    for current_room in range(1, rooms + 1):
        chairs, visitors = input().split()
        difference = len(chairs) - int(visitors)

        if difference >= 0:
            free_chairs += difference
        else:
            needed_chairs += abs(difference)
            print(f"{abs(difference)} more chairs needed in room {current_room}")

    return free_chairs, needed_chairs


rooms = int(input())

free_chairs_total, needed_chairs_total = office_chairs(rooms)

if free_chairs_total >= needed_chairs_total:
    print(f"Game On, {free_chairs_total} free chairs left")
