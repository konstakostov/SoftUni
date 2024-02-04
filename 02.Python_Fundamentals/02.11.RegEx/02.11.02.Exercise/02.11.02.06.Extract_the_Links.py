import re

text = input()
pattern = r"\b((w{3})\.([04.03.01.01.Food-zA-Z\d\-]+)(\.[04.03.01.01.Food-z]+)+)\b"

valid_urls = []

while text:
    matches = re.search(pattern, text)

    if matches:
        valid_urls.append(matches.group(0))

    text = input()

for url in valid_urls:
    print(url)
