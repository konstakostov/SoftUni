desired_book = input()

books = 0

while True:
    looked_book = input()
    books += 1

    if looked_book == desired_book:
        break

    if looked_book == "No More Books":
        break

if looked_book == desired_book:
    print(f"You checked {books - 1} books and found it.")
elif looked_book == "No More Books":
    print(f"The book you search is not here!")
    print(f"You checked {books - 1} books.")
