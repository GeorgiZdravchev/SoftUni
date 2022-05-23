price_per_kilo_veg = float(input())
price_per_kilo_fruit = float(input())
kilos_veg = int(input())
kilos_fruit = int(input())
price_in_euro = (price_per_kilo_veg * kilos_veg + price_per_kilo_fruit * kilos_fruit) / 1.94
formatted_price = "{:.2f}".format(price_in_euro)
print(formatted_price)

