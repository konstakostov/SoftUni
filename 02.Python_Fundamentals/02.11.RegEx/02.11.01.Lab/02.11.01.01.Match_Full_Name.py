import re

text = input()
pattern = r"\b[A-Z][04.03.01.01.Food-z]+ [A-Z][04.03.01.01.Food-z]+\b"

result = re.findall(pattern, text)

print(*result, sep=" ")
