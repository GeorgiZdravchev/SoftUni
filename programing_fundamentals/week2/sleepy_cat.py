from math import ceil, floor
free_days = int(input())
work_days = 365 - free_days
play_time = free_days * 127 + work_days * 63
if play_time < 30000 :
    play_time_one = 30000 - play_time
    formatted_hours = floor(play_time_one / 60)
    hours_in_minutes = int(formatted_hours) * 60
    formatted_minutes = (f"{int(play_time_one) - int(hours_in_minutes) :.0f}")
    print("Tom sleeps well")
    print(f"{formatted_hours} hours and {formatted_minutes} minutes less for play")
elif play_time > 30000 :
    play_time_two = play_time - 30000
    formatted_hours = floor(play_time_two / 60)
    hours_in_minutes = int(formatted_hours) * 60
    formatted_minutes = (f"{int(play_time_two) - int(hours_in_minutes) :.0f}")
    print("Tom will run away")
    print(f"{formatted_hours} hours and {formatted_minutes} minutes more for play")