actor = input()
points_academy = float(input())
judges = int(input())
point_sum = 0
point_judge = 0
for i in range(1, judges + 1):
    judge_name = input()
    points_judge = float(input())
    point_judge = len(judge_name) * points_judge / 2 + point_judge
    if point_judge + points_academy > 1250.5:
        break
point_sum = point_judge + points_academy
diff = abs(1250.5 - point_sum)
if point_sum >= 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {point_sum:.1f}!")
elif point_sum < 1250.5:
    print(f"Sorry, {actor} you need {diff:.1f} more!")

