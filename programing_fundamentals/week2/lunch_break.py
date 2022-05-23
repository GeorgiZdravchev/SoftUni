from math import ceil
serial = input()
episode_duration = int(input())
break_duration = int(input())
time_for_lunch = 0.125 * break_duration
time_for_rest = 0.25 * break_duration
time_left = break_duration - time_for_rest - time_for_lunch
time_left_two = ceil(abs(time_left - episode_duration))
if time_left >= episode_duration :
    print(f"You have enough time to watch {serial} and left with {time_left_two} minutes free time.")
else :
    print(f"You don't have enough time to watch {serial}, you need {time_left_two} more minutes.")