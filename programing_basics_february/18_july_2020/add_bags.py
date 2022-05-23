price_for_20 = float(input())
kilos = float(input())
days = int(input())
luggage = int(input())
price_of_luggage = 0
if kilos < 10:
    price_of_luggage = 0.2 * price_for_20
elif 10 <= kilos <= 20:
    price_of_luggage = 0.5 * price_for_20
else:
    price_of_luggage = price_for_20
if days > 30:
    price_of_luggage += price_of_luggage * 0.1
elif 7 <= days <= 30:
    price_of_luggage += price_of_luggage * 0.15
else:
    price_of_luggage += price_of_luggage * 0.4
print(f"The total price of bags is: {price_of_luggage * luggage:.2f} lv.")
