distance = int(input())
travel_time = input()

if travel_time == "day":
    taxi_fare_day = 0.70 + (0.79 * distance)
    bus_fare = 0.09 * distance
    train_fare = 0.06 * distance

    if distance >= 100:
        print(f"{train_fare:.2f}")
    elif distance >= 20:
        print(f"{bus_fare:.2f}")
    else:
        print(f"{taxi_fare_day:.2f}")

if travel_time == "night":
    taxi_fare_night = 0.70 + (0.90 * distance)
    bus_fare = 0.09 * distance
    train_fare = 0.06 * distance

    if distance >= 100:
        print(f"{train_fare:.2f}")
    elif distance >= 20:
        print(f"{bus_fare:.2f}")
    else:
        print(f"{taxi_fare_night:.2f}")
