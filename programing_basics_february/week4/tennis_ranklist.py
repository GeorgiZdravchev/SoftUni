from math import floor
tournaments = int(input())
starting_points = int(input())
points = 0
total_points = 0
w = 0
average = 0
for i in range(1, tournaments + 1):
    result = input()
    if result == "W":
        w += 1
        points += 2000
    elif result == "F":
        points += 1200
    elif result == "SF":
        points += 720
average = floor(points / tournaments)
total_points = points + starting_points
w_p = w / tournaments * 100
print(f"Final points: {total_points}")
print(f"Average points: {average}")
print(f"{w_p:.2f}%")

