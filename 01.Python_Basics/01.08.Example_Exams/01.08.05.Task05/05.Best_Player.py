most_goals = 0
best_player = ""

while True:
    player = input()

    if player == "END":
        break

    goals = int(input())

    if goals >= 10:
        print(f"{player} is the best player!")
        print(f"He has scored {goals} goals and made a hat-trick !!!")
        raise SystemExit

    if goals > most_goals:
        most_goals = goals
        best_player = player

if most_goals < 3:
    print(f"{best_player} is the best player!")
    print(f"He has scored {most_goals} goals.")
else:
    print(f"{best_player} is the best player!")
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
