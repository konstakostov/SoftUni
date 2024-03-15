goal = 10000
steps_total = 0

while steps_total < goal:
    steps = input()

    if steps == "Going home":
        steps_total += int(input())
        break

    steps_total += int(steps)

if steps_total >= goal:
    print(f"Goal reached! Good job!")
    print(f"{steps_total - goal} steps over the goal!")
else:
    print(f"{goal - steps_total} more steps to reach goal.")
