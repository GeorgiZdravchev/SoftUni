kilometers = int(input())
time = input()
formatted_price = 0
if kilometers < 20 and time == "day" :
   price = 0.7 + kilometers * 0.79
   formatted_price = "{:.2f}".format(price)

elif kilometers < 20 and time == "night" :
    price = 0.7 + kilometers * 0.9
    formatted_price = "{:.2f}".format(price)
elif 20 <= kilometers < 100 :
    price = kilometers * 0.09
    formatted_price = "{:.2f}".format(price)
elif kilometers >= 100 :
    price_train = kilometers * 0.06
    formatted_price = "{:.2f}".format(price_train)
print(formatted_price)
