group = int(input())
days = int(input())

total_coins = 0
coins_per_person = int(total_coins / group)

for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        group -= 2

    if current_day % 15 == 0:
        group += 5

    total_coins += 50
    total_coins -= group * 2

    if current_day % 3 == 0:
        total_coins -= group * 3

    if current_day % 5 == 0:
        total_coins += group * 20
        if current_day % 3 == 0:
            total_coins -= group * 2

coins_per_person = int(total_coins / group)

print(f"{group} companions received {coins_per_person} coins each.")
