from collections import deque


def stock_availability(items, *args):
    inventory = deque(items)

    if args[0] == "delivery":
        for arg in args[1::]:
            inventory.append(arg)

    elif args[0] == "sell":
        if len(args) == 1:
            inventory.popleft()

        else:
            for arg in args[1::]:
                if type(arg) == int:
                    for _ in range(arg):
                        inventory.popleft()
                    continue

                if arg in inventory:
                    while arg in inventory:
                        inventory.remove(arg)

    inventory = list(inventory)

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
