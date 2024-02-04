neighbourhood = [int(x) for x in input().split("@")]
house_index = 0
houses_num = len(neighbourhood)

while True:
    command = input()

    if command == "Love!":
        break

    command, index = command.split()
    index = int(index)

    if command == "Love!":
        break

    house_index += index

    while not 0 <= house_index < len(neighbourhood):
        house_index = 0

    else:
        if neighbourhood[house_index] == 0:
            print(f"Place {house_index} already had Valentine's day.")
            continue
        else:
            neighbourhood[house_index] -= 2
            if neighbourhood[house_index] == 0:
                print(f"Place {house_index} has Valentine's day.")

print(f"Cupid's last position was {house_index}.")

fails = 0

for fail_search in neighbourhood:
    if fail_search != 0:
        fails += 1

if fails == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {fails} places.")
