import math

record_seconds = float(input())
distance_meters = float(input())
seconds_per_meter = float(input())

time_per_data = distance_meters * seconds_per_meter

decline = math.floor(distance_meters / 50)
decline_time = decline * 30

time_total = time_per_data + decline_time

if time_total < record_seconds:
    print(f"Yes! The new record is {time_total:.2f} seconds.")
else:
    print(f"No! He was {abs(record_seconds - time_total):.2f} seconds slower.")
