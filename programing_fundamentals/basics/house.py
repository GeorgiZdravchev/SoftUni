x = float(input())
y = float(input())
h = float(input())
sides = 2 * x * y - 1.5 * 1.5 * 2
back = x * x * 2 - 1.2 * 2
paint_needed = (sides + back) / 3.4
roof_sides = 2 * x * y
roof_back = 2 * (x * h / 2)
paint_needed_roof = (roof_back + roof_sides) / 4.3
formatted_paint_needed = "{:.2f}".format(paint_needed)
formatted_paint_needed_roof = "{:.2f}".format(paint_needed_roof)
print(formatted_paint_needed)
print(formatted_paint_needed_roof)

