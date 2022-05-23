chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
type_of_day = input()
price = 0
if season in "Spring Summer":
    price = chrysanthemums * 2 + roses * 4.1 + tulips * 2.5
elif season in "Autumn Winter":
    price = chrysanthemums * 3.75 + roses * 4.5 + tulips * 4.15
if type_of_day == "Y":
    new_price = price + price * 0.15
elif type_of_day == "N":
    new_price = price
if tulips > 7 and season == "Spring":
    new_price -= new_price * 0.05
if roses >= 10 and season == "Winter":
    new_price -= new_price * 0.1
if roses + tulips + chrysanthemums > 20:
    new_price -= new_price * 0.2
whole_price = new_price + 2
print(f"{whole_price:.2f}")