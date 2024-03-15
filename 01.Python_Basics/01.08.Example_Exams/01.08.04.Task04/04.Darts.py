player = input()

score = 301
good_shots = 0
bad_shots = 0

while True:
    command = input()

    if command == "Retire":
        print(f"{player} retired after {bad_shots} unsuccessful shots.")
        break

    points = int(input())

    if command == "Single":
        if points <= score and (score - points * 1) >= 0:
            score -= points * 1
            good_shots += 1
        else:
            score = score
            bad_shots += 1

    elif command == "Double":
        if points <= score and (score - points * 2) >= 0:
            score -= points * 2
            good_shots += 1
        else:
            score = score
            bad_shots += 1

    elif command == "Triple":
        if points <= score and (score - points * 3) >= 0:
            score -= points * 3
            good_shots += 1
        else:
            score = score
            bad_shots += 1

    if score == 0:
        print(f"{player} won the leg with {good_shots} shots.")
        break
