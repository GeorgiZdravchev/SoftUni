percent_fat = int(input())
percent_protein = int(input())
percent_carbohydrates = int(input())
calories = float(input())
percent_water = float(input())
grams_fat = percent_fat / 100 * calories / 9
grams_protein = percent_protein / 100 * calories / 4
grams_carbohydrates = percent_carbohydrates / 100 * calories / 4
food_weight = grams_carbohydrates + grams_fat + grams_protein
calories_per_gram = calories / food_weight
left_percent = 100 - percent_water
sda = left_percent / 100 * calories_per_gram
print(f"{sda:.4f}")