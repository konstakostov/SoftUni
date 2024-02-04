days = int(input())

money_won = 0
raised_money = 0

wins = 0
losses = 0

wins_total = 0
losses_total = 0


for i in range(1, days + 1):
    while True:
        sport = input()

        if sport == "Finish":
            if wins > losses:
                money_won += money_won * 0.10
            raised_money += money_won
            wins = 0
            losses = 0
            money_won = 0
            break

        while True:
            status = input()

            if status == "win":
                money_won += 20
                wins += 1
                wins_total += 1
                break

            if status == "lose":
                money_won += 0
                losses += 1
                losses_total += 1
                break

if wins_total > losses_total:
    raised_money += raised_money * 0.20
    print(f"You won the tournament! Total raised money: {raised_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {raised_money:.2f}")
