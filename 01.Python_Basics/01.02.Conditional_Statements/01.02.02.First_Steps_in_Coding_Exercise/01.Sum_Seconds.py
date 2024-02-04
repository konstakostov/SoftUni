import math

time_first = int(input())
time_second = int(input())
time_third = int(input())

time_total = time_first + time_second + time_third

minutes = time_total // 60
minutes = math.floor(minutes)

seconds = time_total % 60

if seconds <10:
    print(f"{minutes}:0{seconds}")

else:
    print(f"{minutes}:{seconds}")