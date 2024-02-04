num_cars = int(input())

parking_lot = set()

for _ in range(num_cars):
    direction, car_number = input().split(', ')

    if direction == "IN":
        if car_number not in parking_lot:
            parking_lot.add(car_number)
    elif direction == "OUT":
        if car_number in parking_lot:
            parking_lot.remove(car_number)

if parking_lot:
    print(*parking_lot, sep='\n')
else:
    print("Parking Lot is Empty")

