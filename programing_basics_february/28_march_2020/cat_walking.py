minutes = int(input())
walks = int(input())
calories = int(input())
sum_of_minutes = minutes * walks
calories_burnt = 5 * sum_of_minutes
calories_intake = calories / 2
if calories_intake <= calories_burnt:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burnt}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burnt}.")