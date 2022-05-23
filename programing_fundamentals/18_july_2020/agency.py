name = input()
tickets_for_adults = int(input())
tickets_for_kids = int(input())
price_for_adults = float(input())
tax = float(input())
price_for_kids = price_for_adults - price_for_adults * 0.7
full_price_for_adults = tax + price_for_adults
full_price_for_kids = tax + price_for_kids
full_price = tickets_for_kids * full_price_for_kids + tickets_for_adults * full_price_for_adults
profit = full_price * 0.2
print(f"The profit of your agency from {name} tickets is {profit:.2f} lv.")