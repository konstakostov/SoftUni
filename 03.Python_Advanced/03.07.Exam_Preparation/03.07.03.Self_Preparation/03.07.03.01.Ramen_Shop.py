from collections import deque

bowls = deque(int(x) for x in input().split(', '))
customers = deque(int(x) for x in input().split(', '))

while len(bowls) and len(customers):
    bowl = bowls.pop()
    customer = customers.popleft()

    if bowl > customer:
        bowl -= customer
        bowls.append(bowl)

    elif bowl < customer:
        customer -= bowl
        customers.appendleft(customer)

if customers:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
else:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls)}")
