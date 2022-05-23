length = int(input())
width = int(input())
height = int(input())
percent = float(input())
volume = length * width * height
volume_in_liters = volume * 0.001
taken_percent = percent / 100
needed_water = volume_in_liters * (1 - taken_percent)
print(needed_water)