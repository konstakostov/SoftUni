while True:
    line = input()      # Input String

    if line == "End":   # Break if End Appears
        break

    if line == "SoftUni":       # Skip if SoftUni appears
        continue

    for ch in line:         # Read each character and then print it twice
        print(f"{ch}{ch}", end="")

    print()
