free_days = int(input())

work_days = 365 - free_days

play_time_work = work_days * 63
play_time_free = free_days * 127

play_time_norm = 30000
play_time_real = play_time_work + play_time_free

if play_time_real > play_time_norm:
    print("Tom will run away")
    play_time_above_norm = play_time_real - play_time_norm
    play_time_hours = play_time_above_norm // 60
    play_time_minutes = play_time_above_norm % 60
    print(f"{play_time_hours} hours and {play_time_minutes} minutes more for play")
else:
    print("Tom sleeps well")
    play_time_left = play_time_norm - play_time_real
    play_time_hours = play_time_left // 60
    play_time_minutes = play_time_left % 60
    print(f"{play_time_hours} hours and {play_time_minutes} minutes less for play")

