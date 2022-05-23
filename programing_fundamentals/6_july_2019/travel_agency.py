city = input()
packet = input()
vip = input()
days = int(input())
price_per_day = 0
full_price = 0
condition = True
if days < 1:
    condition = False
    print("Days must be positive number!")
elif not city in "Bansko Borovets Varna Burgas" or not packet in "noEquipment  withEquipment noBreakfast withBreakfast":
    condition = False
    print("Invalid input!")
if city in "Bansko Borovets":
    if packet == "withEquipment":
        price_per_day = 100
        if vip == "yes":
            price_per_day -= price_per_day * 0.1
    elif packet == "noEquipment":
        price_per_day = 80
        if vip == "yes":
            price_per_day -= price_per_day * 0.05
elif city in "Varna Burgas":
    if packet == "withBreakfast":
        price_per_day = 130
        if vip == "yes":
            price_per_day -= price_per_day * 0.12
    elif packet == 'noBreakfast':
        price_per_day = 100
        if vip == "yes":
            price_per_day -= price_per_day * 0.07
full_price = price_per_day * days
if days > 7:
    full_price -= price_per_day
if condition:
    print(f"The price is {full_price:.2f}lv! Have a nice time!")

