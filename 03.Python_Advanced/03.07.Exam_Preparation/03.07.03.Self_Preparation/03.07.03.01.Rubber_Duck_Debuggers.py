from collections import deque

times = deque([int(x) for x in input().split()])
tasks = deque([int(x) for x in input().split()])

vader_ducky = 0
thor_ducky = 0
blue_ducky = 0
yellow_ducky = 0

while times and tasks:
    time = times.popleft()
    task = tasks.pop()

    result = time * task

    if 0 <= result <= 60:
        vader_ducky += 1

    elif 61 <= result <= 120:
        thor_ducky += 1

    elif 121 <= result <= 180:
        blue_ducky += 1

    elif 181 <= result <= 240:
        yellow_ducky += 1

    else:
        tasks.append(task - 2)
        times.append(time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {vader_ducky}")
print(f"Thor Ducky: {thor_ducky}")
print(f"Big Blue Rubber Ducky: {blue_ducky}")
print(f"Small Yellow Rubber Ducky: {yellow_ducky}")
