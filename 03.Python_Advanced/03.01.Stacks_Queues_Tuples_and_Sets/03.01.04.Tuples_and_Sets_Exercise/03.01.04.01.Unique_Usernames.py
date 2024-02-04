num_usernames = int(input())

unique_names = set()

for _ in range(num_usernames):
    username = input()

    unique_names.add(username)

print('\n'.join(unique_names))
