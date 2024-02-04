sub_strings = input().split("|")
sub_list = []

for sub in sub_strings[::-1]:
    sub_list.extend(sub.split())

print(*sub_list)

# sub_strings = [sub.split() for sub in input().split('|')]
# print(*[' '.join(sub) for sub in sub_strings[::-1]])
