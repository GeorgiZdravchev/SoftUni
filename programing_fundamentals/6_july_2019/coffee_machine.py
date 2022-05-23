type_of_drink = input()
sugar = input()
number_of_drinks = int(input())
price_per_espresso = 0
price_per_cappuccino = 0
price_per_tea = 0
full_price = 0
if type_of_drink == "Espresso":
    if sugar == "Without":
        price_per_espresso = 0.9
    elif sugar == "Normal":
        price_per_espresso = 1
    elif sugar == "Extra":
        price_per_espresso = 1.2
elif type_of_drink == "Cappuccino":
    if sugar == "Without":
        price_per_cappuccino = 1
    elif sugar == "Normal":
        price_per_cappuccino = 1.2
    elif sugar == "Extra":
        price_per_cappuccino = 1.6
elif type_of_drink == "Tea":
    if sugar == "Without":
        price_per_tea = 0.5
    elif sugar == "Normal":
        price_per_tea = 0.6
    elif sugar == "Extra":
        price_per_tea = 0.7
full_price_espresso = number_of_drinks * price_per_espresso
full_price_cappuccino = number_of_drinks * price_per_cappuccino
full_price_tea = number_of_drinks * price_per_tea
if sugar == "Without" and type_of_drink == "Espresso":
    full_price_espresso -= full_price_espresso * 0.35
elif sugar == "Without" and type_of_drink == "Cappuccino":
    full_price_cappuccino -= full_price_cappuccino * 0.35
elif sugar == "Without" and type_of_drink == "Tea":
    full_price_tea -= full_price_tea * 0.35
if type_of_drink == "Espresso" and number_of_drinks >= 5:
    full_price_espresso -= full_price_espresso * 0.25
if full_price_espresso > 15:
    full_price_espresso -= full_price_espresso * 0.2
elif full_price_cappuccino > 15:
    full_price_cappuccino -= full_price_cappuccino * 0.2
elif full_price_tea > 15:
    full_price_tea -= full_price_tea * 0.2
if type_of_drink == "Espresso":
    print(f"You bought {number_of_drinks} cups of Espresso for {full_price_espresso:.2f} lv.")
elif type_of_drink == "Cappuccino":
    print(f"You bought {number_of_drinks} cups of Cappuccino for {full_price_cappuccino:.2f} lv.")
elif type_of_drink == "Tea":
    print(f"You bought {number_of_drinks} cups of Tea for {full_price_tea:.2f} lv.")