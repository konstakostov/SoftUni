pirates = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
MAX_HEALTH = int(input())

while True:
    command = input().split()
    action = command[0]
    if action == "Retire":
        break

    if action == "Fire":
        fire_index = int(command[1])
        fire_damage = int(command[2])

        if 0 <= fire_index < len(warship):
            warship[fire_index] -= fire_damage
            if warship[fire_index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit(0)

    elif action == "Defend":
        defend_index_start = int(command[1])
        defend_index_end = int(command[2])
        defend_damage = int(command[3])

        if 0 <= defend_index_start < len(pirates) and 0 <= defend_index_end < len(pirates):
            for defend_index in range(defend_index_start, defend_index_end + 1):
                pirates[defend_index] -= defend_damage
                if pirates[defend_index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit(0)

    elif action == "Repair":
        repair_index = int(command[1])
        repair_health = int(command[2])

        if 0 <= repair_index < len(pirates):
            pirates[repair_index] += repair_health
            if pirates[repair_index] > MAX_HEALTH:
                pirates[repair_index] = MAX_HEALTH

    elif action == "Status":
        sections_to_repair = 0

        for section in pirates:
            if section < (int(MAX_HEALTH * 0.20)):
                sections_to_repair += 1

        print(f"{sections_to_repair} sections need repair.")

print(f"Pirate ship status: {sum(pirates)}")
print(f"Warship status: {sum(warship)}")
