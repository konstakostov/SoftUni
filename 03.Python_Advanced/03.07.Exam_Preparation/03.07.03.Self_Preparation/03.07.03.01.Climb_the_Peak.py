from collections import deque

portions = deque([int(x) for x in input().split(", ")])
stamina = deque([int(x) for x in input().split(", ")])

peaks_difficulty = {
    80: "Vihren",
    90: "Kutelo",
    100: "Banski Suhodol",
    60: "Polezhan",
    70: "Kamenitza",
}

peaks_climbed = []
index = 0

for difficulty, peak in peaks_difficulty.items():
    if not portions or not stamina:
        break
    while True:
        food = portions.pop()
        energy = stamina.popleft()

        total = food + energy

        if total >= difficulty:
            peaks_climbed.append(peak)
            break
        else:
            if not portions or not stamina:
                break
            continue

if len(peaks_climbed) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if peaks_climbed:
    print(f"Conquered peaks:")
    print(*peaks_climbed, sep='\n')
