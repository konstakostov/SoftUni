student_total = 0
standard_total = 0
kid_total = 0

while True:
    movie = input()
    if movie == "Finish":
        break

    capacity = int(input())
    sold_tickets = 0

    while sold_tickets < capacity:
        ticket = input()

        if ticket == "End":
            break

        if ticket == "student":
            student_total += 1
        elif ticket == "standard":
            standard_total += 1
        elif ticket == "kid":
            kid_total += 1

        sold_tickets += 1

    print(f"{movie} - {((sold_tickets / capacity) * 100):.2f}% full.")

tickets_total = student_total + standard_total + kid_total

print(f"Total tickets: {tickets_total}")
print(f"{((student_total / tickets_total) * 100):.2f}% 04.10.02.04.Student tickets.")
print(f"{((standard_total / tickets_total) * 100):.2f}% standard tickets.")
print(f"{((kid_total / tickets_total) * 100):.2f}% kids tickets.")
