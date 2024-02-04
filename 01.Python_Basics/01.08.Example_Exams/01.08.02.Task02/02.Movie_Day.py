time = int(input())
scenes = int(input())
scenes_time = int(input())

time *= 0.85

time_filming = scenes * scenes_time

if time_filming <= time:
    print(f"You managed to finish the movie on time! You have {round(time - time_filming)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(time_filming - time)} minutes.")

