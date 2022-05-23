wanted_profit = int(input()) * 100
# * 100 промени надолу
profit = 0
condition = True
for i in range(0, wanted_profit + 1):
    name = input()
    if name == "Party!":
        condition = False
        break
    cocktails = int(input())
    price_cocktail = len(name) * cocktails
    if price_cocktail % 2 == 1:
        price_cocktail -= price_cocktail * 0.25
    profit += price_cocktail
    if profit * 100 >= wanted_profit:
        print("Target acquired.")
        break
diff = abs((wanted_profit - profit * 100) / 100)
if not condition:
    print(f"We need {diff:.2f} leva more.")
print(f'Club income - {profit:.2f} leva.')
