hours = int(input())
minutes = int(input())
hour = 0
minute = 0
if 45 <= minutes <= 59 :
    minute = (minutes + 15) % 60
    if hours == 23 :
        hour == 0
        if minute < 9:
            print(f"{hour}:0{minute}")
        else:
            print(f"{hour}:{minute}")
    else:
        hour = hours + 1
        if minute < 9:
            print(f"{hour}:0{minute}")
        else:
            print(f"{hour}:{minute}")
else:
    hour = hours
    minute = minutes + 15
    if minute < 9 :
        print(f"{hour}:0{minute}")
    else:
        print(f"{hour}:{minute}")