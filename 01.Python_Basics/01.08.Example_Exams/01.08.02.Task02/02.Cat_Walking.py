minutes_for_walk = int(input())
walks_per_day = int(input())
calories_intake = float(input())

calories_burned = (minutes_for_walk * 5) * walks_per_day

calories_intake_half = calories_intake / 2

if calories_burned >= calories_intake_half:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")
