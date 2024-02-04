current_deck = input().split()
num_shuffles = int(input())

for shuffle in range(num_shuffles):
    shuffled_deck = []

    middle_deck = len(current_deck) // 2

    left_deck = current_deck[0: middle_deck]
    right_deck = current_deck[middle_deck::]

    for card_index in range(len(left_deck)):
        shuffled_deck.append(left_deck[card_index])
        shuffled_deck.append(right_deck[card_index])

    current_deck = shuffled_deck

print(current_deck)
