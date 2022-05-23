season = input()
group = input()
students = int(input())
nights = int(input())
sport = "as"
price = 0
if group in "girls boys" :
    if season == "Winter":
        price_per_night = 9.6
    elif season == "Spring":
        price_per_night = 7.2
    elif season == "Summer":
        price_per_night = 15
elif group == "mixed":
    if season == "Winter":
        price_per_night = 10
    elif season == "Spring":
        price_per_night = 9.5
    elif season == "Summer":
        price_per_night = 20
price = price_per_night * nights * students
if students >= 50:
    price -= price * 0.5
elif 20 <= students < 50:
    price -= price * 0.15
elif 10 <= students < 20:
    price -= price * 0.05
if group == "girls":
    if season == "Winter":
        sport = "Gymnastics"
    elif season == "Spring":
        sport = "Athletics"
    elif season == "Summer":
        sport = "Volleyball"
if group == "boys":
    if season == "Winter":
        sport = "Judo"
    elif season == "Spring":
        sport = "Tennis"
    elif season == "Summer":
        sport = "Football"
elif group == "mixed":
    if season == "Winter":
        sport = "Ski"
    elif season == "Spring":
        sport = "Cycling"
    elif season == "Summer":
        sport = "Swimming"
print(f"{sport} {price:.2f} lv.")