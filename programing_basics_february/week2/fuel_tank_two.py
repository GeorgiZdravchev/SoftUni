fuel_type = input()
fuel_amount = float(input())
club_card = input()
price_discount = 0
if club_card == "Yes" :
    gasoline = 2.04
    diesel = 2.21
    gas = 0.85
    if fuel_type == "Gas" :
        price = fuel_amount * gas
        if 20 <= fuel_amount <= 25:
            price_discount = price - 0.08 * price
        elif 25 <= fuel_amount :
            price_discount = price - 0.1 * price
    elif fuel_type == "Gasoline" :
        price = fuel_amount * gasoline
        if 20 <= fuel_amount <= 25:
            price_discount = price - 0.08 * price
        elif 25 <= fuel_amount :
            price_discount = price - 0.1 * price
    elif fuel_type == "Diesel" :
        price = fuel_amount * diesel
        if 20 <= fuel_amount <= 25:
            price_discount = price - 0.08 * price
        elif 25 <= fuel_amount :
            price_discount = price - 0.1 * price
        else :
            price_discount = price
elif club_card == "No" :
    gasoline = 2.22
    diesel = 2.33
    gas = 0.93
    if fuel_type == "Gas" :
        price = fuel_amount * gas
        if 20 <= fuel_amount <= 25:
            price_discount = price - 0.08 * price
        elif 25 <= fuel_amount :
            price_discount = price - 0.1 * price
    elif fuel_type == "Gasoline" :
        price = fuel_amount * gasoline
        if 20 <= fuel_amount <= 25:
            price_discount = price - 0.08 * price
        elif 25 <= fuel_amount :
            price_discount = price - 0.1 * price
    elif fuel_type == "Diesel" :
        price = fuel_amount * diesel
        if 20 <= fuel_amount <= 25:
            price_discount = price - 0.08 * price
        elif 25 <= fuel_amount :
            price_discount = price - 0.1 * price
        else :
            price_discount = price

price_discount_format = "{:.2f}".format(price_discount)
print(f"{price_discount_format} lv.")