dungeon_rooms = input().split("|")
MAX_HEALTH = 100
health = 100
bitcoins = 0
room_counter = 0

for room in dungeon_rooms:
    command, amount = room.split()

    if command == "potion":
        room_counter += 1
        if health + int(amount) > MAX_HEALTH:
            print(f"You healed for {MAX_HEALTH - health} hp.")
            health = MAX_HEALTH
        else:
            print(f"You healed for {int(amount)} hp.")
            health += int(amount)
        print(f"Current health: {health} hp.")

    elif command == "chest":
        room_counter += 1
        bitcoins += int(amount)
        print(f"You found {amount} bitcoins.")

    else:
        room_counter += 1
        health -= int(amount)
        if health > 0:
            print(f"You slayed {command}.")

        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_counter}")
            exit(0)

print("You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")








# dungeon = input().split("|")
#
# initial_health = 100
# current_health = initial_health
# bitcoins = 0
#
# alive = True
# room_counter = 0
#
# for room in dungeon:
#     room_counter += 1
#
#     command, amount = room.split()
#
#     if command == "potion":
#         current_health += int(amount)
#         if current_health > initial_health:
#             partial_heal = int(amount) - (current_health - initial_health)
#             current_health = initial_health
#             print(f"You healed for {partial_heal} hp.")
#         else:
#             print(f"You healed for {amount} hp.")
#         print(f"Current health: {current_health} hp.")
#
#     elif command == "chest":
#         bitcoins += int(amount)
#         print(f"You found {amount} bitcoins.")
#
#     else:
#         current_health -= int(amount)
#         if current_health > 0:
#             print(f"You slayed {command}.")
#         else:
#             alive = False
#             print(f"You died! Killed by {command}.")
#             print(f"Best room: {room_counter}")
#             break
#
# if alive:
#     print("You've made it!")
#     print(f"Bitcoins: {bitcoins}")
#     print(f"Health: {current_health}")
