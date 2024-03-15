# # 01. Invert Values
# numbers = input().split()
#
# opposite_numbers = []
#
# for i in numbers:
#     num = int(i)
#
#     opposite_numbers.append(-num)
#
# print(opposite_numbers)
#


# # 02. Multiple Lis
# factor = int(input())
# count = int(input())
#
# multiples = []
#
# for i in range(1, count + 1):
#     multiples.append(i * factor)
#
# print(multiples)
#


# 03. Football Cards
# cards = input().split(" ")
#
# team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
# team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
#
# game_termination = False
#
# for player in cards:
#     if player in team_a:
#         team_a.remove(player)
#     elif player in team_b:
#         team_b.remove(player)
#
#     if len(team_a) < 7 or len(team_b) < 7:
#         game_termination = True
#         break
#
# print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
#
# if game_termination:
#     print("Game was terminated")
#


# # 04. Number Beggars
# earned_money = input().split(", ")
#
# earned_money_digits = []
#
# for i in earned_money:
#     earned_money_digits.append(int(i))
#
# beggars_count = int(input())
#
# output = []
# start_index = 0
#
# while start_index < beggars_count:
#     beggars_earnings = 0
#
#     for current_index in range(start_index, len(earned_money_digits), beggars_count):
#         beggars_earnings += earned_money_digits[current_index]
#     output.append(beggars_earnings)
#
#     start_index += 1
#
# print(output)
#


# # 05. Faro Shuffle
# card_deck = input().split(" ")
# shuffles = int(input())
#
# for current_shuffle in range(shuffles):
#     shuffled_deck = []
#
#     middle_of_deck = len(card_deck) // 2
#
#     left_deck = card_deck[0:middle_of_deck]
#     right_deck = card_deck[middle_of_deck::]
#
#     for current_index in range(middle_of_deck):
#         shuffled_deck.append(left_deck[current_index])
#         shuffled_deck.append(right_deck[current_index])
#
#     card_deck = shuffled_deck
#
# print(card_deck)
#


# 06. Survival of the Biggest
# numbers_list = input().split()
# numbers_list_as_digits = []
#
# for num in numbers_list:
#     numbers_list_as_digits.append(int(num))
#
# num_to_remove = int(input())
#
# for i in range(num_to_remove):
#     numbers_list_as_digits.remove(min(numbers_list_as_digits))
#
# print(*numbers_list_as_digits, sep=", ")












