w = float(input())
h = float(input())
desks_per_row = (h * 100 - 100) // 70
rows = w * 100 // 120
places = desks_per_row * rows - 3
print(places)