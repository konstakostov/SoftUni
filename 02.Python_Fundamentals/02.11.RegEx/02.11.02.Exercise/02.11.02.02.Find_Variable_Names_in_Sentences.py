import re

text = input()

pattern = r"\b_([04.03.01.01.Food-zA-Z0-9]+)\b"

matches = re.findall(pattern, text)

print(','.join(matches))
