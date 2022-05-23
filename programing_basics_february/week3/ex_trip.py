budget = float(input())
season = input()
price = 0
destination = ''
type_of_place = ''
if 0 < budget <= 100:
   destination = "Bulgaria"
   if season == "summer":
      price = budget * 0.3
   elif season == "winter":
       price = budget * 0.7
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.4
    elif season == "winter":
        price = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    price = 0.9 * budget
if season == "summer" and destination in "Bulgaria Balkans":
    type_of_place = "Camp"
else:
    type_of_place = "Hotel"
print(f"Somewhere in {destination}")
print(f"{type_of_place} - {price:.2f}")





