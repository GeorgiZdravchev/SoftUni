chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())
price_of_chicken = chicken_menu * 10.35
price_of_fish = fish_menu * 12.40
price_of_vegetarian = vegetarian_menu * 8.15
sum_before_dessert = price_of_vegetarian + price_of_fish + price_of_chicken
price_of_dessert = 0.2 * sum_before_dessert
full_price = sum_before_dessert + price_of_dessert + 2.50
formatted_price = "{:.2f}".format(full_price)
print(formatted_price)