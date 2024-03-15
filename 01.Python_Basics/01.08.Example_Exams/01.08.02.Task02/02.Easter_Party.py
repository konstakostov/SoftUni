guests = int(input())
deposit = float(input())
budget = float(input())

cake = budget * 0.10

if 10 <= guests <= 15:
    deposit *= 0.85
elif 15 < guests <= 20:
    deposit *= 0.80
elif guests > 20:
    deposit *= 0.75
else:
    deposit *= 1

total_costs = (guests * deposit) + cake

if total_costs <= budget:
    print(f"It is party time! {(budget - total_costs):.2f} leva left.")
else:
    print(f"No party! {(total_costs - budget):.2f} leva needed.")
