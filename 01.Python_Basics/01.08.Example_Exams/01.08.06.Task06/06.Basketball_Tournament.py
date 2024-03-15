games_won = 0
games_lost = 0
games_total = 0

while True:
    tournament = input()

    if tournament == "End of tournaments":
        print(f"{((games_won / games_total) * 100):.2f}% matches win")
        print(f"{((games_lost / games_total) * 100):.2f}% matches lost")
        break

    number_of_games = int(input())
    games_total += number_of_games

    for game in range(1, number_of_games + 1):
        points_desi = int(input())
        points_other = int(input())

        if points_desi > points_other:
            games_won += 1
            print(f"Game {game} of tournament {tournament}: win with {points_desi - points_other} points.")
        else:
            games_lost += 1
            print(f"Game {game} of tournament {tournament}: lost with {points_other - points_desi} points.")
