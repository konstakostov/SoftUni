# # 01. Invert Values
# elements = input().split()
#
# result = []
#
# for el in elements:
#     num = int(el)
#
#     result.append(-num)
#
# print(result)
#


# # 02. Multiple 04.10.01.03.List
# factor = int(input())
# count = int(input())
#
# result = []
#
# for multiplier in range(1, count + 1):
#     result.append(multiplier * factor)
#
# print(result)
#


# # 03. Football Cards, Version 01
# cards = input().split()
#
# team_a_players = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# team_b_players = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
# game_terminate = False
#
# for current_card in cards:
#     if "A-" in current_card:
#         for i in team_a_players:
#             if str(i) in current_card:
#                 team_a_players.remove(i)
#
#     elif "B-" in current_card:
#         for j in team_a_players:
#             if str(j) in current_card:
#                 team_b_players.remove(j)
#
#     if len(team_a_players) < 7 or len(team_b_players) < 7:
#         game_terminate = True
#         break
#
# print(f"Team A - {len(team_a_players)}; Team B - {len(team_b_players)}")
# if game_terminate:
#     print("Game was terminated")
#

# # 03. Football Cards, Version 02
# cards = input().split()
#
# team_a_sent_off = []
# team_b_sent_off = []
#
# terminate_game = False
#
# for card in cards:
#     if card in team_a_sent_off or card in team_b_sent_off:
#         continue
#
#     card_args = card.split("-")
#     team_name = card_args[0]
#     team_number = card_args[1]
#
#     is_first_team = team_name == "A"
#     if is_first_team == "A":
#         team_a_sent_off.append(card)
#     else:
#         team_b_sent_off.append(card)
#
#     if len(team_a_sent_off) > 4 or len(team_b_sent_off) > 4:
#         terminate_game = True
#         break
#
# initial_players = 11
# team_a_left = initial_players - len(team_a_sent_off)
# team_b_left = initial_players - len(team_b_sent_off)
#
# print(f"Team A - {team_a_left}; Team B - {team_b_left}")
#
# if terminate_game:
#     print("Game was terminated")
#

# # 03. Football Cards, Version 03
# players = input().split()
#
# team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
# team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "b-11"]
#
# game_termination = False
#
# for player in players:
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
# money_list = input().split(", ")    # ["1", "2", "3", "4", "5"]
#
# money_list_as_digit = []
#
# for element in money_list:
#     money_list_as_digit.append(int(element))    # money_list_as_digit = [1, 2, 3, 4, 5]
#
# num_beggars = int(input())
#
# final_sums = []
# starting_index = 0
#
# while starting_index < num_beggars:
#     sum_current_beggar = 0
#
#     for current_index in range(starting_index, len(money_list_as_digit), num_beggars):
#         sum_current_beggar += money_list_as_digit[current_index]
#
#     final_sums.append(sum_current_beggar)
#
#     starting_index += 1
#
# print(final_sums)
#


# # 05. Faro Shuffle
# deck_of_cards = input().split()
# shuffles = int(input())
#
# for shuffle in range(shuffles):
#     final_deck = []
#
#     middle_deck = len(deck_of_cards) // 2
#
#     left_part = deck_of_cards[0: middle_deck]
#     right_part = deck_of_cards[middle_deck::]
#
#     for card_index in range(len(left_part)):
#         final_deck.append(left_part[card_index])
#         final_deck.append((right_part[card_index]))
#
#     deck_of_cards = final_deck
#
# print(deck_of_cards)
#



# 06. Survival of the Biggest









# 07. *Easter Gifts









# 08. *Seize the Fire









# 09. *Hello, France









# 10. *Bread Factory








