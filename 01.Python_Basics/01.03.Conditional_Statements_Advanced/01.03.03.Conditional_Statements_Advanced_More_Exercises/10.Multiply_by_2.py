while True:
    number = float(input())

    if number < 0:
        print(f"Negative number!")
        break

    number *= 2
    print(f"Result: {number:.2f}")
