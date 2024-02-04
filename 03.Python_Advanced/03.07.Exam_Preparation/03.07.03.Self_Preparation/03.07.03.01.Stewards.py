from collections import deque

seats = deque(x for x in input().split(', '))
seq_one = deque(int(x) for x in input().split(', '))
seq_two = deque(int(x) for x in input().split(', '))

seat_matches = []
rotations = 0

while True:
    if rotations == 10:
        break
    if len(seat_matches) == 3:
        break

    num_one = seq_one.popleft()
    num_two = seq_two.pop()

    letter = chr(num_one + num_two)

    seat_one = str(num_one) + letter
    seat_two = str(num_two) + letter

    if seat_one in seat_matches or seat_two in seat_matches:
        rotations += 1
        continue

    if seat_one not in seats and seat_two not in seats:
        seq_one.append(num_one)
        seq_two.appendleft(num_two)

    elif seat_one in seats:
        seat_matches.append(seat_one)
    elif seat_two in seats:
        seat_matches.append(seat_two)

    rotations += 1

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")
