name = input()
points = float(input())
judges = int(input())

for i in range(1, judges + 1):
    j_name = input()
    j_score = float(input())

    points += (len(j_name) * j_score) / 2

    if points > 1250.5:
        print(f"Congratulations, {name} got a nominee for leading role with {points:.1f}!")
        break

if points <= 1250.5:
    print(f"Sorry, {name} you need {(1250.5 - points):.1f} more!")
