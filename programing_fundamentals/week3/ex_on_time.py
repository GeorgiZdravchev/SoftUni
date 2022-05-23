hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())
total_time_exam = hour_of_exam * 60 + minutes_of_exam
total_time_arrival = hour_of_arrival * 60 + minutes_of_arrival
diff = abs(total_time_arrival - total_time_exam)
hours = diff // 60
minutes = diff % 60
if total_time_arrival == total_time_exam or 0 < total_time_exam - total_time_arrival <= 30:
    if diff == 0:
        print("On time")
    else:
        print("On time")
        print(f"{diff} minutes before the start")
elif total_time_arrival > total_time_exam:
    print("Late")
    if hours == 0:
        print(f"{minutes} minutes after the start")
    else:
        print(f"{hours} : {minutes:02d} hours after the start")
elif 30 < total_time_arrival < total_time_exam:
    print("Early")
    if hours == 0:
        print(f"{minutes} minutes before the start")
    else:
        print(f"{hours}:{minutes:02d} hours before the start")