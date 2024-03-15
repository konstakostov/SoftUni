def numbers_searching(*args):
    args = sorted(args)
    last_arg = args[0]

    missing = 0
    duplicates = []

    for arg in args:
        if args.count(arg) > 1 and arg not in duplicates:
            duplicates.append(arg)

        if arg - 2 == last_arg:
            missing = arg - 1

        last_arg = arg

    return [missing, duplicates]


print(numbers_searching(1, 2, 4, 2, 5, 4))

print()

print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print()

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
