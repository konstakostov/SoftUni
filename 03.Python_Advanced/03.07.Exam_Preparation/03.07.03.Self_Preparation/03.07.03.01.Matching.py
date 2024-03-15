from collections import deque

males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])

matches = 0

while males and females:
    if females[0] <= 0:
        females.popleft()
        continue
    elif females[0] % 25 == 0:
        for _ in range(2):
            females.popleft()
        continue

    if males[-1] <= 0:
        males.pop()
        continue
    elif males[-1] % 25 == 0:
        for _ in range(2):
            males.pop()
        continue

    woman = females.popleft()
    man = males.pop()

    if woman == man:
        matches += 1
    else:
        man -= 2
        males.append(man)


print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join([str(x) for x in males][::-1])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")
