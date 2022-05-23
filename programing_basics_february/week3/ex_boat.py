budget = int(input())
season = input()
fishermen = int(input())
price_of_boat = 0
if season == "Spring":
    price_of_boat = 3000
elif season in "Summer Autumn":
    price_of_boat = 4200
elif season == "Winter":
    price_of_boat = 2600
if fishermen <= 6:
    price_of_boat -= price_of_boat * 0.1
elif 6 < fishermen <= 11:
    price_of_boat -= price_of_boat * 0.15
elif fishermen >= 12:
    price_of_boat -= price_of_boat * 0.25
if fishermen % 2 == 0 and season != "Autumn":
    price_of_boat -= price_of_boat * 0.05
diff = abs(budget - price_of_boat)
if budget >= price_of_boat:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")