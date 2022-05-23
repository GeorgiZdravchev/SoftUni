from math import ceil
height_of_wall = int(input())
width_of_wall = int(input())
percent = int(input())
full_space = 4 * height_of_wall * width_of_wall
space_to_paint = ceil(full_space - (full_space * percent / 100))
amount_of_paint = 0
condition = True
for i in range(0, space_to_paint + 1):
    inpt = input()
    if inpt == "Tired!":
        condition = False
        break
    paint = int(inpt)
    amount_of_paint += paint
    if amount_of_paint >= space_to_paint:
        break
diff = abs(space_to_paint - amount_of_paint)

if not condition:
    print(f"{diff} quadratic m left.")
if space_to_paint == amount_of_paint:
    print("All walls are painted! Great job, Pesho!")
elif space_to_paint < amount_of_paint:
    print(f"All walls are painted and you have {diff} l paint left!")