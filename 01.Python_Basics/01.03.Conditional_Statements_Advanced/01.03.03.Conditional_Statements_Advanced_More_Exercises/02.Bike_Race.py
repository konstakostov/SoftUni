# Number of Junior and Senior Cyclists and the Type of Track
juniors = int(input())
seniors = int(input())
track = input()

# Pricing
money_for_participation_jun = 0
money_for_participation_sen = 0
participants_total = juniors + seniors

if track == "trail":
    money_for_participation_jun = 5.50
    money_for_participation_sen = 7
elif track == "cross-country":
    if participants_total < 50:
        money_for_participation_jun = 8
        money_for_participation_sen = 9.50
    else:
        money_for_participation_jun = 8 - 8 * 0.25
        money_for_participation_sen = 9.50 - 9.50 * 0.25

elif track == "downhill":
    money_for_participation_jun = 12.25
    money_for_participation_sen = 13.75

elif track == "road":
    money_for_participation_jun = 20
    money_for_participation_sen = 21.50

# Money Made
money_jun_total = money_for_participation_jun * juniors
money_sen_total = money_for_participation_sen * seniors
costs = (money_jun_total + money_sen_total) * 0.05

money_total = (money_jun_total + money_sen_total) - costs

print(f"{money_total:.2f}")
