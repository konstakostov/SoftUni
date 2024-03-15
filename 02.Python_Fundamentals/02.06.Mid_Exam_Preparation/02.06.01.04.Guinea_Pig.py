food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000

days = 30

for current_day in range(1, days + 1):
    food -= 300

    if current_day % 2 == 0:
        hay -= food * 0.05

    if current_day % 3 == 0:
        cover -= weight / 3

    if food <= 0 or hay <= 0 or cover <= 0:
        print("Merry must go to the pet store!")
        exit(0)

print(f"Everything is fine! Puppy is happy! Food: {food/1000:.2f}, Hay: {hay/1000:.2f}, Cover: {cover/1000:.2f}.")
