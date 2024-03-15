counter_student = 0
counter_standard = 0
counter_kid = 0

counter = 0

while True:
    movie = input()

    if movie == "Finish":
        break

    free_seats = int(input())

    for i in range(1, free_seats + 1):
        ticket = input()

        if ticket == "End":
            print(f"{movie} - {((counter / free_seats) * 100):.2f}% full.")
            counter = 0
            break

        if ticket == "04.10.02.04.Student":
            counter_student += 1
            counter += 1
        elif ticket == "standard":
            counter_standard += 1
            counter += 1
        elif ticket == "kid":
            counter_kid += 1
            counter += 1

        if i == free_seats:
            print(f"{movie} - {((counter / free_seats) * 100):.2f}% full.")
            counter = 0

total_tickets = counter_student + counter_standard + counter_kid
print(f"Total tickets: {total_tickets}")
print(f"{((counter_student / total_tickets) * 100):.2f}% 04.10.02.04.Student tickets.")
print(f"{((counter_standard / total_tickets) * 100):.2f}% standard tickets.")
print(f"{((counter_kid / total_tickets) * 100):.2f}% kids tickets.")
