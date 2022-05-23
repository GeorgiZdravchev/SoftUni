from math import floor
record = float(input())
distance = float(input())
seconds_per_meter = float(input())
time = distance * seconds_per_meter
time_reduction = distance // 15 * 12.5
total_time = time + time_reduction
time_diff = total_time - record
formatted_time_diff = "{:.2f}".format(time_diff)
formatted_total_time = "{:.2f}".format(total_time)
if total_time >= record :
    print(f"No, he failed! He was {formatted_time_diff} seconds slower.")
else :
    print(f"Yes, he succeeded! The new world record is {formatted_total_time} seconds.")

