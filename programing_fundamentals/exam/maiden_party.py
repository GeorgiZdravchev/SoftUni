party_price = float(input())
love_letters = int(input())
roses = int(input())
key_chains = int(input())
drawings = int(input())
surprises = int(input())
all_products = love_letters + roses + key_chains + drawings + surprises
first_sum = love_letters * 0.6 + roses * 7.2 + key_chains * 3.6 + drawings * 18.2 + surprises * 22
if all_products >= 25:
    first_sum -= first_sum * 0.35
first_sum -= first_sum * 0.1
diff = abs(first_sum - party_price)
if first_sum >= party_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f'Not enough money! {diff:.2f} lv needed.')