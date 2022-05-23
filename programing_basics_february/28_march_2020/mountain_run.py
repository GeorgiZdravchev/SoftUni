record = float(input())
distance = float(input())
time = float(input())
slow = distance // 50
time_for_climb = time * distance + slow * 30
diff = abs(record - time_for_climb)
if record <= time_for_climb:
    print(f"No! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {time_for_climb:.2f} seconds.")