occurrences = {}

for char in list(input()):
    occurrences[char] = occurrences.get(char, 0) + 1

for symbol, times in sorted(occurrences.items()):
    print(f"{symbol}: {times} time/s")
