num_guests = int(input())

reservations = set()

for _ in range(num_guests):
    codes = input()
    reservations.add(codes)

while True:
    ticket = input()

    if ticket == "END":
        break

    if ticket in reservations:
        reservations.remove(ticket)

print(len(reservations))
for el in sorted(reservations):
    print(el)
