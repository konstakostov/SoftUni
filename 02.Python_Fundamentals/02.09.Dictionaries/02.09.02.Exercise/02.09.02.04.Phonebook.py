data = input()
phonebook = {}

while "-" in data:
    name = data.split("-")[0]
    number = data.split("-")[1]

    if name not in phonebook:
        phonebook[name] = 0

    phonebook[name] = number

    data = input()

num_contacts = int(data)

for i in range(num_contacts):
    name = input()

    if name not in phonebook:
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phonebook[name]}")
