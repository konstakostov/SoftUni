banned_words = input().split(", ")
text = input()

for banned in banned_words:
    while banned in text:
        text = text.replace(banned, "*" * len(banned))

print(text)
