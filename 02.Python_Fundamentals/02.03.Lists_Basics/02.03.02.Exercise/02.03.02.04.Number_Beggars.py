money_given = input().split(", ")

money_given_as_number = []

for money in money_given:
    money_given_as_number.append(int(money))

num_beggars = int(input())

final_sum = []
starting_index = 0

while starting_index < num_beggars:
    current_beggar_sum = 0

    for current_index in range(starting_index, len(money_given_as_number), num_beggars):
        current_beggar_sum += money_given_as_number[current_index]

    final_sum.append(current_beggar_sum)

    starting_index += 1

print(final_sum)
