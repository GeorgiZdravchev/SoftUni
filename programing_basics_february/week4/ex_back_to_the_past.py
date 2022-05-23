money = float(input())
year = int(input())
age = 18
years = year - 1799
needed_money = 0
money_for_year = 0
money_for_odd_year = 0
new_age = 0
for i in range(0, years):
    if i % 2 == 0:
        money_for_odd_year += 12000
        new_age = 19 + i
    else:
        needed_money += 12000 + new_age * 50
    money_for_year = money_for_odd_year + needed_money
diff = abs(money - money_for_year)
if money > money_for_year:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")

