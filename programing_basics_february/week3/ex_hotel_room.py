month = input()
nights = int(input())
price_of_studio = 0
price_of_apartment = 0
if month in "May October":
    price_of_studio = 50 * nights
    price_of_apartment = 65 * nights
    if 14 >= nights > 7:
        price_of_studio -= price_of_studio * 0.05
    elif 14 < nights:
        price_of_studio -= price_of_studio * 0.3
elif month in "June September":
    price_of_studio = 75.20 * nights
    price_of_apartment = 68.70 * nights
    if nights > 14:
        price_of_studio -= price_of_studio * 0.2
elif month in "July August":
    price_of_studio = 76 * nights
    price_of_apartment = 77 * nights
if nights > 14:
    price_of_apartment -= price_of_apartment * 0.1
print(f"Apartment: {price_of_apartment:.2f} lv.")
print(f"Studio: {price_of_studio:.2f} lv.")