hours = int(input())
minutes = int(input()) + 15

if minutes > 59:
    hours = hours + 1
    minutes = minutes - 60

if hours >= 24:
    hours = hours - 24

if minutes >= 10:
    print(f"{hours}:{minutes}")
else:
    print(f"{hours}:0{minutes}")