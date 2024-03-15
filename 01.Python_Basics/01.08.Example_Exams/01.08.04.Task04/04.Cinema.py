capacity = int(input())

seats_left = capacity
counter = 0

income = 0

while True:
    command = input()

    if command == "Movie time!":
        print(f"There are {seats_left} seats left in the cinema.")
        break

    seats = int(command)

    if seats_left - seats >= 0:
        seats_left -= seats
        counter += seats
        if seats % 3 == 0:
            income += (seats * 5) - 5
        else:
            income += seats * 5
    else:
        print(f"The cinema is full.")
        break

print(f"Cinema income - {income} lv.")
