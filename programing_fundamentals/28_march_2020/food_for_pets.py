days = int(input())
all_food = float(input())
i = 1
dog = 0
cat = 0
food_eaten = 0
biscuits = 0
food_for_the_day = 0
while i < days + 1:
    ate_by_dog = int(input())
    ate_by_cat = int(input())
    dog += ate_by_dog
    cat += ate_by_cat
    food_for_the_day = ate_by_cat + ate_by_dog
    food_eaten += food_for_the_day

    if i % 3 == 0:
        biscuits += food_for_the_day * 0.1
    i += 1
print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{food_eaten / all_food * 100:.2f}% of the food has been eaten.")
print(f"{dog / food_eaten * 100:.2f}% eaten from the dog.")
print(f"{cat / food_eaten * 100:.2f}% eaten from the cat.")



