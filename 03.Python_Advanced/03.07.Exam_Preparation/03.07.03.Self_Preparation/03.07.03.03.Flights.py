def flights(*args):
    airport = {}

    data_length = len(args)

    for index in range(0, data_length + 1, 2):
        if args[index] == "Finish":
            break

        destination = args[index]
        passengers = args[index + 1]

        if destination not in airport:
            airport[destination] = 0

        airport[destination] += int(passengers)

    return airport


print(flights('Vienna', 256,
              'Vienna', 26,
              'Morocco', 98,
              'Paris', 115,
              'Finish',
              'Paris', 15))

print()

print(flights('London', 0,
              'New York', 9,
              'Aberdeen', 215, 'Sydney', 2,
              'New York', 300,
              'Nice', 0,
              'Finish'))

print()

print(flights('Finish',
              'New York', 90,
              'Aberdeen', 300,
              'Sydney', 0))
