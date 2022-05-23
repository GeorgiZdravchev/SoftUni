pens = int(input())
marker = int(input())
liters = int(input())
discount_percent = int(input())
discount = discount_percent / 100
price_of_pens = pens * 5.80
price_of_markers = marker * 7.20
price_of_cleaner = liters * 1.20
sum_of_all = price_of_cleaner + price_of_pens + price_of_markers
money_needed = sum_of_all - (sum_of_all * discount)
formatted_price = "{:.2f}".format(money_needed)
print(formatted_price)