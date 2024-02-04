from collections import deque

effects = deque([int(x) for x in input().split(', ')])
casings = deque([int(x) for x in input().split(', ')])

datura = 0
cherry = 0
decoy = 0

while effects and casings:
    effect = effects.popleft()
    casing = casings.pop()

    bomb = effect + casing

    if bomb == 40:
        datura += 1

    elif bomb == 60:
        cherry += 1

    elif bomb == 120:
        decoy += 1

    else:
        casing -= 5

        effects.appendleft(effect)
        casings.append(casing)

    if datura >= 3 and cherry >= 3 and decoy >= 3:
        break


if datura >= 3 and cherry >= 3 and decoy >= 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in effects])}")
else:
    print("Bomb Effects: empty")

if casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in casings])}")
else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry}")
print(f"Datura Bombs: {datura}")
print(f"Smoke Decoy Bombs: {decoy}")
