screening_type = input()
rows = int(input())
columns = int(input())
seating = columns * rows
price = 0
if screening_type == "Premiere":
    price = seating * 12
elif screening_type == "Normal":
    price = seating * 7.5
elif screening_type == "Discount":
    price = seating * 5
print(f"{price:.2f} leva")