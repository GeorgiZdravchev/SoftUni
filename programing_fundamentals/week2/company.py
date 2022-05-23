from math import floor
hours = int(input())
days =  int(input())
workers = int(input())
work_hours = (days - 0.1 * days) * 8
work_overtime = workers * 2 * days
total_hours = work_hours + work_overtime
formatted_hours = floor(total_hours)
if formatted_hours >= hours :
    hours_left = formatted_hours - hours
    print(f"Yes!{hours_left} hours left.")
elif formatted_hours <= hours :
    hours_needed = hours - formatted_hours
    print(f"Not enough time!{hours_needed} hours needed.")