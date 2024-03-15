import re

text = input()
pattern = r"\s(([04.03.01.01.Food-zA-Z0-9]+[04.03.01.01.Food-zA-Z0-9\.\-\_]+)@([04.03.01.01.Food-zA-Z\-]+(\.[04.03.01.01.Food-zA-Z\-]+)+))\b"


matches = re.findall(pattern, text)

for match in matches:
    print(match[0])
