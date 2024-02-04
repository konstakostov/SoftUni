import math

world_record = float(input())
distance = float(input())
time_per_meter = float(input())

time_needed = distance * time_per_meter

water_resistance = math.floor(distance // 15)

time_needed += water_resistance * 12.5

if time_needed < world_record:
    print(f"Yes, he succeeded! The new world record is {(time_needed):.2f} seconds.")
else:
    print(f"No, he failed! He was {(time_needed - world_record):.2f} seconds slower.")

# # WORLD SWIMMING RECORD VARIANT 2
# import math
#
# record_in_seconds = float(input())
# record_in_meters = float(input())
# seconds_per_meter = float(input())
#
# water_resistance_seconds = math.floor(record_in_meters / 15) * 12.5
# swimmer_seconds = seconds_per_meter * record_in_meters + water_resistance_seconds
#
# if swimmer_seconds >= record_in_seconds:
#     print(f"No, he failed! He was {(swimmer_seconds- record_in_seconds):.2f} seconds slower.")
# else:
#     print(f"Yes, he succeeded! The new world record is {swimmer_seconds:.2f} seconds.")
