season = input()
group_type = input()
students_count = int(input())
nights = int(input())

cost_per_night = 0
sport = ""

if season == "Winter":
    if group_type == "boys":
        cost_per_night = 9.60
        sport = "Judo"
    elif group_type == "girls":
        cost_per_night = 9.60
        sport = "Gymnastics"
    elif group_type == "mixed":
        cost_per_night = 10
        sport = "Ski"

elif season == "Spring":
    if group_type == "boys":
        cost_per_night = 7.20
        sport = "Tennis"
    elif group_type == "girls":
        cost_per_night = 7.20
        sport = "Athletics"
    elif group_type == "mixed":
        cost_per_night = 9.50
        sport = "Cycling"

elif season == "Summer":
    if group_type == "boys":
        cost_per_night = 15
        sport = "Football"
    elif group_type == "girls":
        cost_per_night = 15
        sport = "Volleyball"
    elif group_type == "mixed":
        cost_per_night = 20
        sport = "Swimming"

total_price = cost_per_night * nights * students_count

if students_count >= 50:
    total_price *= 0.50
elif 20 <= students_count < 50:
    total_price *= 0.85
elif 10 <= students_count < 20:
    total_price *= 0.95

print(f"{sport} {total_price:.2f} lv.")
