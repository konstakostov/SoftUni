actor = input()
points = float(input())
judges = int(input())

for _ in range(1, judges + 1):
    judge_name = input()
    judge_points = float(input())

    points += (len(judge_name) * judge_points) / 2

    if points > 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {points:.1f}!")
        break
else:
    print(f"Sorry, {actor} you need {(1250.5 - points):.1f} more!")
