pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())
hours_per_day = pages / pages_per_hour / number_of_days
formatted_hours = "{:.0f}".format(hours_per_day)
print(formatted_hours)