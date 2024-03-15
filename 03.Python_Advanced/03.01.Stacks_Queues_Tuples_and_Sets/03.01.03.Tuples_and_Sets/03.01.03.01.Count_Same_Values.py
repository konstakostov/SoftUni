numbers = tuple(input().split())

occurrences = {}

for num in numbers:
    if num not in occurrences:
        occurrences[num] = 0
    occurrences[num] += 1

for number, count in occurrences.items():
    print(f"{float(number):.1f} - {count} times")
