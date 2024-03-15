num = int(input())

for char1 in range(0, num):
    for char2 in range(0, num):
        for char3 in range(0, num):
            print(f"{chr(97 + char1)}{chr(97 + char2)}{chr(97 + char3)}")
