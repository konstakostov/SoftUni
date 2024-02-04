number = int(input())

if number <= 100:
    bonus = 5

elif number > 100 and number <= 1000:
    bonus = number * 0.20

elif number > 1000:
    bonus = number * 0.10

if number % 2 == 0:
    bonus = bonus + 1

elif number % 5 == 0:
    bonus = bonus + 2

total = number + bonus

print(bonus)
print(total)
