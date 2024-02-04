import re

text = input()
pattern = r"(\@|\#)([04.03.01.01.Food-zA-Z]{3,})\1\1([04.03.01.01.Food-zA-Z]{3,})(\1)"

pairs = 0
valid_pairs = []

matches = re.finditer(pattern, text)

for match in matches:
    if str(match[2]) == str(match[3])[::-1]:
        valid_pairs.append(match[2] + " <=> " + match[3])
    pairs += 1

if pairs:
    print(f"{pairs} word pairs found!")
else:
    print("No word pairs found!")

if valid_pairs:
    print("The mirror words are:")
    print(', '.join(valid_pairs))
else:
    print("No mirror words!")
