n = int(input())
word = input()

strings_list = []
new_strings_list = []

for i in range(n):
    current_string = input()

    strings_list.append(current_string)

    if word in current_string:
        new_strings_list.append(current_string)

print(strings_list)
print(new_strings_list)
