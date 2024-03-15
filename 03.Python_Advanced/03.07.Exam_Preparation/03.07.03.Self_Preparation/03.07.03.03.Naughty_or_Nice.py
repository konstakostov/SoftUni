def naughty_or_nice_list(santas_list, *args, **kwargs):
    result = []
    nice_list = []
    naughty_list = []

    def placing_kids():
        if len(kids) == 1:
            if alignment == "Nice":
                nice_list.append(kids[0][1])
            elif alignment == "Naughty":
                naughty_list.append(kids[0][1])
            santas_list.remove(*kids)

    for kids in args:
        num, alignment = kids.split("-")
        kids = [x for x in santas_list if x[0] == int(num)]
        placing_kids()

    for name, alignment in kwargs.items():
        kids = [x for x in santas_list if x[1] == name]
        placing_kids()

    if nice_list:
        result.append(f"Nice: {', '.join(nice_list)}")
    if naughty_list:
        result.append(f"Naughty: {', '.join(naughty_list)}")
    if santas_list:
        result.append(f"Not found: {', '.join([x[1] for x in santas_list])}")

    return '\n'.join(result)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print()

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print()

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
