food_bought = int(input())
food_bought_kilos = food_bought * 1000
food_eaten = 0
while True:
    food = input()
    if food == "Adopted":
        break
    food = int(food)
    food_eaten += food
diff = abs(food_bought_kilos - food_eaten)
if food_bought_kilos >= food_eaten:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")

