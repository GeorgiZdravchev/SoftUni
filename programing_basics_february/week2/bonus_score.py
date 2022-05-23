number = int(input())
bonus = 0
if number <= 100 :
    bonus_points = 5
    if number % 2 == 0 :
       bonus_points = bonus_points + 1
    elif number % 5 ==0 :
        bonus_points = bonus_points + 2
elif 100 < number <= 1000:
    bonus_points = 0.2 * number
    if number % 2 == 0 :
        bonus_points = bonus_points + 1
    elif number % 5 ==0 :
        bonus_points = bonus_points + 2
else :
    bonus_points = 0.1 * number
    if number % 2 == 0 :
        bonus_points = bonus_points + 1
    elif number % 5 ==0 :
        bonus_points = bonus_points + 2
sum = number + bonus_points
print(bonus_points)
print(sum)