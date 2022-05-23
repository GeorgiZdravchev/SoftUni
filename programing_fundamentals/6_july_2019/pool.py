from math import ceil
people = int(input())
tax = float(input())
shezlong = float(input())
umbrella = float(input())
entrance_price = people * tax
people_for_shezlong = 0.75 * people
people_for_umbrella = 0.5 * people
price_shezlong = ceil(people_for_shezlong) * shezlong
price_umbrella = ceil(people_for_umbrella) * umbrella
full_price = entrance_price + price_umbrella + price_shezlong
print(f"{full_price:.2f} lv.")