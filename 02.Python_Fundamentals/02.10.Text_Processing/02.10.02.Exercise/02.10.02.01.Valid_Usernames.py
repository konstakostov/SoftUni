# Variant 01
usernames = input().split(", ")

for username in usernames:
    is_valid = True

    if len(username) < 3 or len(username) > 16:
        is_valid = False
        continue

    for char in username:
        if not (char.isalnum() or char == "-" or char == "_"):
            is_valid = False
            continue

    if " " in username:
        is_valid = False
        continue

    if is_valid:
        print(username)


# Variant 02
def is_length(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def is_contained(name):
    if name.isalnum() or "_" in name or "-" in name:
        return True
    return False


def is_redundant(name):
    if " " not in name:
        return True
    return False


def is_valid(name):
    if is_length(name) and is_contained(name) and is_redundant(name):
        return True
    return False


usernames = input().split(", ")

for username in usernames:
    if is_valid(username):
        print(username)

