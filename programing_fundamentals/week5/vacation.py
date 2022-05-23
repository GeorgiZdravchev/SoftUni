money_needed = float(input())
current_money = float(input())
spending_spree = 0
days = 0
condition = True
while spending_spree < 5 and current_money < money_needed:
    action = input()
    money = float(input())
    if action == "save":
        spending_spree = 0
        current_money += money
    elif action == 'spend':
        spending_spree += 1
        current_money -= money
        if current_money < 0:
            current_money = 0
    days += 1
if spending_spree == 5:
    print(f"You can't save the money.")
    print(days)
if current_money >= money_needed:
    print(f"You saved the money for {days} days.")

