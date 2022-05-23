months = int(input())
water_pm = 20
internet_pm = 15
water = 0
electricity = 0
internet = 0
others = 0
average = 0
sum_others = 0
sum_electricity = 0
for i in range(1, months + 1):
    electricity = float(input())
    others = (electricity + water_pm + internet_pm) * 1.2
    sum_others = sum_others + others
    sum_electricity = sum_electricity + electricity
water = months * water_pm
internet = months * internet_pm
average = (water + internet + sum_electricity + sum_others) / months
print(f"Electricity: {sum_electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {sum_others:.2f} lv")
print(f"Average: {average:.2f} lv")