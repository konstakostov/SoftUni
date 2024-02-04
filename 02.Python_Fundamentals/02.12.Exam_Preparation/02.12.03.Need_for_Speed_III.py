num_cars = int(input())

garage = {}

for i in range(num_cars):
    car, mileage, fuel = input().split("|")
    garage[car] = garage.get(car, {'mileage': int(mileage), 'fuel': int(fuel)})

while True:
    command = input()
    if command == "Stop":
        break

    action = command.split(" : ")[0]

    if action == "Drive":
        car = command.split(" : ")[1]
        distance = command.split(" : ")[2]
        fuel = command.split(" : ")[3]

        if garage[car]['fuel'] - int(fuel) > 0:
            garage[car]['mileage'] += int(distance)
            garage[car]['fuel'] -= int(fuel)
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")

        if garage[car]['mileage'] >= 100000:
            print(f"Time to sell the {car}!")
            del garage[car]

    elif action == "Refuel":
        car = command.split(" : ")[1]
        fuel = command.split(" : ")[2]

        if garage[car]['fuel'] + int(fuel) > 75:
            refueled = 75 - garage[car]['fuel']
            garage[car]['fuel'] = 75
            print(f"{car} refueled with {refueled} liters")
        else:
            garage[car]['fuel'] += int(fuel)
            print(f"{car} refueled with {fuel} liters")

    elif action == "Revert":
        car = command.split(" : ")[1]
        kilometers = command.split(" : ")[2]

        if garage[car]['mileage'] - int(kilometers) < 10000:
            garage[car]['mileage'] = 10000
        else:
            garage[car]['mileage'] -= int(kilometers)
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car, value in garage.items():
    print(f"{car} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")
