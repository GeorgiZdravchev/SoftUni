from math import ceil, floor
days = int(input())
left_food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())
dog = days * dog_food
cat = days * cat_food
turtle = days * turtle_food / 1000
total_food = dog + cat + turtle
if total_food <= left_food :
    food_left = left_food - total_food
    formatted_food = floor(food_left)
    print(f"{formatted_food} kilos of food left.")
elif total_food >= left_food :
    food_needed = total_food - left_food
    formatted_food = ceil(food_needed)
    print(f"{formatted_food} more kilos of food are needed.")
