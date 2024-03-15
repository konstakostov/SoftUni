from collections import deque

clients = deque()

while True:
    client = input()

    if client == "End":
        break
    elif client == "Paid":
        while clients:
            print(clients.popleft())
        continue

    clients.append(client)

print(f"{len(clients)} people remaining.")

