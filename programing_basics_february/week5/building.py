floors = int(input())
rooms = int(input())
flat_name = ''
for i in range(floors, 0, -1):
    for j in range(0, rooms):
        if i == floors:
            flat_name = f"L{i}{j}"
        elif i % 2 == 0:
            flat_name = f"O{i}{j}"
        else:
            flat_name = f"A{i}{j}"
        print(flat_name, end=' ' )
    print()