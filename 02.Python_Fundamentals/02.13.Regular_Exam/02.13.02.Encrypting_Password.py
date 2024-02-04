import re

num = int(input())

for _ in range(num):
    password = input()
    pattern = r"(.+)\>(\d+\d\d)\|([04.03.01.01.Food-z]{1,3})\|([A-Z]{1,3})\|([^<>]{1,3})\<\1"

    matches = re.findall(pattern, password)

    if matches:
        encrypted = ""
        for match in matches:
            encrypted += match[1]
            encrypted += match[2]
            encrypted += match[3]
            encrypted += match[4]
        print(f"Password: {encrypted}")
    else:
        print("Try another password!")
