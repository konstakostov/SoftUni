facebook = {}

command = input()
while command != "Log out":
    info = command.split(": ")

    if info[0] == "New follower":
        username = info[1]

        if username not in facebook:
            facebook[username] = facebook.get(username, {'likes': 0, 'comments': 0})

    elif info[0] == "Like":
        username = info[1]
        likes = int(info[2])

        if username not in facebook:
            facebook[username] = facebook.get(username, {'likes': likes, 'comments': 0})
        else:
            facebook[username]['likes'] += likes

    elif info[0] == "Comment":
        username = info[1]

        if username not in facebook:
            facebook[username] = facebook.get(username, {'likes': 0, 'comments': 1})
        else:
            facebook[username]['comments'] += 1

    elif info[0] == "Blocked":
        username = info[1]

        if username not in facebook:
            print(f"{username} doesn't exist.")
        else:
            del facebook[username]

    command = input()

print(f"{len(facebook)} followers")
for username, value in facebook.items():
    print(f"{username}: {value['likes'] + value['comments']}")
