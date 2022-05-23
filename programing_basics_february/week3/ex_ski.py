days = int(input())
place = input()
grade = input()
nights = days - 1
price = 0
discount_price = 0
whole_price = 0
if place == "room for one person":
    discount_price = nights * 18
elif place == "apartment":
    price = nights * 25
    if days < 10:
        discount_price = price - price * 0.3
    elif 10 <= days <= 15:
        discount_price = price - price * 0.35
    else:
        discount_price = price - price * 0.5
elif place == "president apartment":
    price = nights * 35
    if days < 10:
        discount_price = price - price * 0.1
    elif 10 <= days <= 15:
        discount_price = price - price * 0.15
    else:
        discount_price = price - price * 0.2
if grade == "positive":
    whole_price = discount_price + discount_price * 0.25
elif grade == "negative":
    whole_price = discount_price - discount_price * 0.1
print(f"{whole_price:.2f}")