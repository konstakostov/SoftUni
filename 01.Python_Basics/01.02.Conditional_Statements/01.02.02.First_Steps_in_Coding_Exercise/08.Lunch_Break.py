# import math
#
# tv_series = input()
#
# episode_time = int(input())
# break_time = int(input())
#
# lunch_time = break_time / 8
# relax_time = break_time / 4
#
# break_time_left = break_time - (lunch_time + relax_time)
#
# if episode_time < break_time_left:
#     print(f"You have enough time to watch {tv_series} and "
#           f"left with {math.ceil(break_time_left - episode_time)} minutes free time.")
# else:
#     print(f"You don't have enough time to watch {tv_series}, "
#           f"you need {math.ceil(abs(episode_time - break_time_left))} more minutes.")

# LUNCH BREAK VERSION 02
#
# import math
#
# series = input()
# episode_length = int(input())
# break_length = int(input())
#
# lunch_time = break_length / 8
# leisure_time = break_time / 4
#
# time_taken = lunch_time + leisure_time + episode_time
# time_left = break_time - time_taken
#
# if time_left >= 0:
#     print(f"You have enough time to watch {series} and "
#           f"left with {math.ceil(time_left)} minutes free time.")
# else:
#     print(f"You don't have enough time to watch {series}, "
#           f"you need {math.ceil(abs(time_left))} more minutes.")
#