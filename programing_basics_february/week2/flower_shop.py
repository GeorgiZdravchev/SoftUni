from math import floor, ceil
magnolii = int(input())
zyumbyuli = int(input())
roses = int(input())
cactuses = int(input())
price_of_gift = float(input())
magnolii_price = 3.25
zyumbyuli_price = 4
roses_price = 3.5
cactus_price = 8
total = (magnolii * magnolii_price + zyumbyuli * zyumbyuli_price +
         roses * roses_price + cactuses * cactus_price) - (magnolii * magnolii_price + zyumbyuli * zyumbyuli_price +
         roses * roses_price + cactuses * cactus_price) * 0.05
if total >= price_of_gift :
    money_left = total - price_of_gift
    format_money = floor(money_left)
    print(f"She is left with {format_money} leva.")
elif total < price_of_gift :
    money_needed = price_of_gift - total
    format_money = ceil(money_needed)
    print(f"She will have to borrow {format_money} leva.")


