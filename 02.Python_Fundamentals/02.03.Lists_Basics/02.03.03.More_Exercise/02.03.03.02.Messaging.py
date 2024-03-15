sequence = input().split()

message = list(input())

indexes_from_sequence = []
final_message = []

for num in sequence:
    searched_index = 0
    for digit in num:
        searched_index += int(digit)

    if searched_index > len(message) - 1:
        searched_index -= len(message)
        final_message.append(message[searched_index])
        message.remove(message[searched_index])
    else:
        final_message.append(message[searched_index])
        message.remove(message[searched_index])

print("".join(final_message))
