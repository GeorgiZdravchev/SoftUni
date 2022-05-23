from math import ceil
days = int(input())
kilometers_day_one = float(input())
i = 0
all_kilometers = 0
for i in range(days):
    percent = int(input())
    kilometers_next_day = kilometers_day_one * percent / 100 + kilometers_day_one
    all_kilometers += kilometers_day_one
    kilometers_day_one = kilometers_next_day


    i += 1
diff = abs(all_kilometers + kilometers_day_one - 1000)
if all_kilometers + kilometers_day_one >= 1000:
    print(f"You've done a great job running {ceil(diff)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers")

