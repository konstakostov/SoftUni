player_1 = input()
player_2 = input()

points_01 = 0
points_02 = 0

while True:
    command = input()

    if command == "End of game":
        print(f"{player_1} has {points_01} points")
        print(f"{player_2} has {points_02} points")
        break

    card_01 = int(command)
    card_02 = int(input())

    if card_01 > card_02:
        points_01 += card_01 - card_02
    elif card_01 < card_02:
        points_02 += card_02 - card_01
    elif card_01 == card_02:
        print("Number wars!")
        card_03 = int(input())
        card_04 = int(input())
        if card_03 > card_04:
            print(f"{player_1} is winner with {points_01} points")
        elif card_03 < card_04:
            print(f"{player_2} is winner with {points_02} points")
        break
