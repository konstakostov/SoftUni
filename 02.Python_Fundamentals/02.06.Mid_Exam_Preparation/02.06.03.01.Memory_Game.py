sequence = input().split()

counter = 0
game_won = False

while True:
    command = input()
    if command == "end":
        break

    counter += 1
    index_01 = int(command.split()[0])
    index_02 = int(command.split()[1])

    if not 0 <= index_01 < len(sequence) or not 0 <= index_02 < len(sequence) or index_01 == index_02:
        middle_sequence = int(len(sequence)) // 2
        sequence = sequence[:middle_sequence] + [f"-{counter}a"] + [f"-{counter}a"] + sequence[middle_sequence:]
        print("Invalid input! Adding additional elements to the board")

    else:
        element_01 = sequence[index_01]
        element_02 = sequence[index_02]

        if element_01 == element_02:
            print(f"Congrats! You have found matching elements - {element_01}!")
            sequence.remove(element_01)
            sequence.remove(element_02)

        elif sequence[index_01] != sequence[index_02]:
            print("Try again!")

    if len(sequence) < 1:
        game_won = True
        break

if game_won:
    print(f"You have won in {counter} turns!")
else:
    print(f"Sorry you lose :(")
    print(*sequence, sep=" ")
