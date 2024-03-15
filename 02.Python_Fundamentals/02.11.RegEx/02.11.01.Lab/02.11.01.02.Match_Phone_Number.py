import re

numbers = input()

pattern = r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b"

result = re.findall(pattern, numbers)

print(", ".join(result))
