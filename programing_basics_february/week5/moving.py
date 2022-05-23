width_space = int(input())
length_space = int(input())
height_space = int(input())
available_space = width_space * length_space * height_space
occupied_space = 0
while True:
    inpt = input()
    if inpt == "Done":
        break
    occupied_space += int(inpt)
    if occupied_space > available_space:
        break
diff = abs(occupied_space-available_space)
if available_space >= occupied_space:
    print(f"{diff} Cubic meters left.")
else:
    print(f"No more free space! You need {diff} Cubic meters more.")