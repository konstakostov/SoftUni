import re

text = input()

emoji_pattern = r"\:{2}[A-Z][04.03.01.01.Food-z]{2,}\:{2}|\*{2}[A-Z][04.03.01.01.Food-z]{2,}\*{2}"
cool_pattern = r"\d"

emojis = []
emojis_cool = []
cool_threshold = 1

match_digits = re.findall(cool_pattern, text)
for digit in match_digits:
    cool_threshold *= int(digit)

match_emojis = re.findall(emoji_pattern, text)
for emoji in match_emojis:
    emojis.append(emoji)

for emoji in emojis:
    coolness = 0
    for char in emoji:
        if char != "*" and char != ":":
            coolness += ord(char)
    if coolness > cool_threshold:
        emojis_cool.append(emoji)


print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
print('\n'.join(emojis_cool))
