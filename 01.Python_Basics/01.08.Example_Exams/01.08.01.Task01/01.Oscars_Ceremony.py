rent = int(input())

statues = rent * 0.70
catering = statues * 0.85
sound = catering * 0.50

total = rent + statues + catering + sound

print(f"{total:.2f}")
