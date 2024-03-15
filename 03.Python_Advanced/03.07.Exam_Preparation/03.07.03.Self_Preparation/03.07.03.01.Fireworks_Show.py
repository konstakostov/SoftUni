from collections import deque

effects = deque([int(x) for x in input().split(', ')])
powers = deque([int(x) for x in input().split(', ')])

palm = 0
willow = 0
crossette = 0

while effects and powers:
    if palm >= 3 and willow >= 3 and crossette >= 3:
        break

    if effects[0] <= 0:
        effects.popleft()
        continue

    if powers[-1] <= 0:
        powers.pop()
        continue

    effect = effects.popleft()
    power = powers.pop()

    firework = effect + power

    if firework % 3 == 0 and firework % 5 == 0:
        crossette += 1

    elif firework % 3 == 0:
        palm += 1

    elif firework % 5 == 0:
        willow += 1

    else:
        effect -= 1
        effects.append(effect)

        powers.append(power)


if palm >= 3 and willow >= 3 and crossette >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in effects])}")

if powers:
    print(f"Explosive Power left: {', '.join([str(x) for x in powers])}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")
