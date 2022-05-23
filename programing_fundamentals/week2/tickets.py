budget = float(input())
category = input()
people = int(input())
transport = 0
price_of_ticket = 0
if 0 < people <= 4:
    transport = budget * 0.75
elif 4 < people <= 9:
    transport = budget * 0.6
elif 9 < people <= 24:
    transport = budget * 0.5
elif 24 < people <= 49:
    transport = budget * 0.4
else:
    transport = budget * 0.25
remaining_money = budget - transport
if category == "VIP":
    price_of_ticket = 499.99
elif category == "Normal":
    price_of_ticket = 249.99
sum_of_tickets = price_of_ticket * people
diff = abs(remaining_money - sum_of_tickets)
if sum_of_tickets <= remaining_money:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")