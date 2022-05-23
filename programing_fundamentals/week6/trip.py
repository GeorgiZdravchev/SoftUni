condition = False
while True:
    country = input()
    sum_money = 0
    if country == "End":
        break
    money_needed = float(input())
    while money_needed > sum_money:
        savings = float(input())
        sum_money += savings
        if money_needed <= sum_money:
            condition = True
            print(f"Going to {country}!")
