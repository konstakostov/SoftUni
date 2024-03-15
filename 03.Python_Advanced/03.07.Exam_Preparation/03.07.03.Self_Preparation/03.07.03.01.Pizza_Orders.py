from collections import deque

orders = deque([int(x) for x in input().split(', ')])
employees = deque([int(x) for x in input().split(', ')])

pizzas_made = 0

while orders and employees:
    order = orders.popleft()

    if order <= 0 or order > 10:
        continue

    employee = employees.pop()

    if order <= employee:
        pizzas_made += order

    elif order > employee:
        order -= employee
        pizzas_made += employee

        orders.appendleft(order)

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas_made}")
    print(f"Employees: {', '.join(str(x) for x in employees)}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in orders)}")
