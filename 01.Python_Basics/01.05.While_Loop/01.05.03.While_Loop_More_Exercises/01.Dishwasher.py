bottles = int(input())

detergent_total = bottles * 750
per_plate = 5
per_pot = 15

counter = 0
plates = 0
pots = 0

detergent_left = detergent_total

while True:
    command = input()

    if command == "End":
        print(f"Detergent was enough!")
        print(f"{plates} dishes and {pots} pots were washed.")
        print(f"Leftover detergent {round(detergent_left)} ml.")
        break

    quantity = int(command)
    counter += 1

    if counter % 3 == 0:
        detergent_left -= quantity * per_pot
        pots += quantity
    else:
        detergent_left -= quantity * per_plate
        plates += quantity

    if detergent_left <= 0:
        print(f"Not enough detergent, {round(abs(detergent_left))} ml. more necessary!")
        break






# detergent = int(input())
#
# detergent_volume = 750
# dishes_detergent = 5
# pot_detergent = 15
#
# detergent_volume_total = round(detergent_volume * detergent)
#
# dishes_total = 0
# pots_total = 0
# batch_num = 0
#
#
# while detergent_volume_total > 0:
#     command = input()
#
#     if command == "End":
#         print(f"Detergent was enough!")
#         print(f"{dishes_total} dishes and {pots_total} pots were washed.")
#         print(f"Leftover detergent {detergent_volume_total} ml.")
#         break
#
#     units_washed = int(command)
#     batch_num += 1
#
#     if batch_num % 3 == 0:
#         detergent_volume_total -= units_washed * pot_detergent
#         pots_total += units_washed
#
#     else:
#         detergent_volume_total -= units_washed * dishes_detergent
#         dishes_total += units_washed
#
# else:
#     print(f"Not enough detergent, {abs(detergent_volume_total)} ml. more necessary!")
