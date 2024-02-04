pieces_total = int(input()) * int(input())
piece_size = 1

while pieces_total > 0:
    command = input()

    if command == "STOP":
        print(f"{pieces_total} pieces are left.")
        break

    pieces = int(command)
    pieces_total -= pieces

if pieces_total <= 0:
    print(f"No more cake left! You need {abs(pieces_total)} pieces more.")
