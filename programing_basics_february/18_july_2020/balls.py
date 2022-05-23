from math import floor
balls = int(input())
red = 0
orange = 0
yellow = 0
white = 0
black = 0
other = 0
points = 0
for i in range (0, balls):
    ball = input()
    if ball == "red":
        red += 1
        points +=5
    elif ball == "orange":
        orange += 1
        points += 10
    elif ball == "yellow":
        yellow += 1
        points += 15
    elif ball == "white":
        white += 1
        points += 20
    elif ball == "black":
        black += 1
        points = points // 2
    else:
        points = points
        other += 1
print(f"Total points: {points}")
print(f"Red balls: {red}")
print(f"Orange balls: {orange}")
print(f"Yellow balls: {yellow}")
print(f"White balls: {white}")
print(f"Other colors picked: {other}")
print(f"Divides from black balls: {black}")
