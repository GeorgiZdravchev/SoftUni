from math import floor, ceil
x = int(input())
y = float(input())
z = int(input())
workers = int(input())
grape = x * y
wine = 0.4 * grape / 2.5
if wine >= z :
    wine_left = ceil(wine - z)
    liters_per_person = ceil(wine_left / workers)
    formatted_liters = floor(wine)
    print(f"Good harvest this year! Total wine: {formatted_liters} liters.")
    print(f"{wine_left} liters left -> {liters_per_person} liters per person.")
elif wine < z:
    wine_short = z - wine
    formatted_wine = floor(wine_short)
    print(f"It will be a tough winter! More {formatted_wine} liters wine needed.")


