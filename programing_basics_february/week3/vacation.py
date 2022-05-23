budget = float(input())
season = input()
price = 0
destination = "as"
type_of_place = "as"
if 0 <= budget <= 1000:
    type_of_place = "Camp"
    if season == "Summer":
        destination = "Alaska"
        price = 0.65 * budget
    elif season == "Winter":
        destination = "Morocco"
        price = 0.45 * budget
elif 1000 < budget <= 3000:
    type_of_place = "Hut"
    if season == "Summer":
        destination = "Alaska"
        price = 0.8 * budget
    elif season == "Winter":
        destination = "Morocco"
        price = 0.6 * budget
elif 3000 < budget:
    type_of_place = "Hotel"
    if season == "Summer":
        destination = "Alaska"
    elif season == "Winter":
        destination = "Morocco"
    price = 0.9 * budget
print(f"{destination} - {type_of_place} - {price:.2f}")
