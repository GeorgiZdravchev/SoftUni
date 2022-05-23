budget = float(input())
nights = int(input())
price_per_night = float(input())
percent = int(input())
total_price_nights = 0
sum_percent = 0
total_price = 0
if nights > 7:
    price_per_night -= price_per_night * 0.05
total_price_nights = nights * price_per_night
sum_percent = budget * (percent / 100)
total_price = sum_percent + total_price_nights
diff = abs(budget - total_price)
if total_price <= budget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")
