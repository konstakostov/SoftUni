import math

series = input()
seasons = int(input())
episodes = int(input())
time = int(input())

ads = time * 0.20
extra_time = seasons * 10
time += ads

time_needed = time * episodes * seasons + extra_time
print(f"Total time needed to watch the {series} series is {math.floor(time_needed)} minutes.")
