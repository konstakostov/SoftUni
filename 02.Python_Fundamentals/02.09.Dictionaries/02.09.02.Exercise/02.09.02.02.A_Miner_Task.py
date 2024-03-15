command = input()
counter = 0

resources = {}

while command != "stop":
    counter += 1

    if counter % 2 != 0:
        resource = command
        if resource not in resources:
            resources[resource] = 0
    else:
        quantity = int(command)
        resources[resource] += quantity

    command = input()

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")
