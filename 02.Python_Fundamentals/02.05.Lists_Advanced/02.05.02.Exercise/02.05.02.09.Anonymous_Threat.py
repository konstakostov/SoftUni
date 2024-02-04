text = input().split()

command = input()

while command != "3:1":
    command = command.split()

    if command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])

        if 0 <= start_index < len(text) and 0 <= end_index < len(text):
            text[start_index: end_index] = [''.join(text[start_index: end_index])]

        elif 0 <= start_index < len(text) and not 0 <= end_index < len(text):
            text[start_index::] = [''.join(text[start_index::])]

        elif not 0 <= start_index < len(text) and 0 <= end_index < len(text):
            text[:end_index] = [''.join(text[:end_index])]

    elif command[0] == "divide":
        index = int(command[1])
        partitions = int(command[2])

        divided_partitions = [""] * partitions
        counter_partitions = 1
        counter_index = 0

        for char in text[index]:
            divided_partitions[counter_index].append(char)
            if counter_partitions + 1 == partitions:
                counter_partitions = 1
                counter_index += 1
            else:
                counter_partitions += 1

        if len(divided_partitions[-1]) < partitions:
            divided_partitions[-2: -1] = [''.join(divided_partitions[-2: -1])]

        text[index] = divided_partitions

    command = input()

print(' '.join(text))
