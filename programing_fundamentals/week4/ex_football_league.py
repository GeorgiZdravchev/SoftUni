capacity = int(input())
fans = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0
percent_a = 0
percent_b = 0
percent_v = 0
percent_g = 0
average = 0
for ch in range(1, fans + 1):
    sector = input()
    if sector == 'A':
        sector_a += 1
    if sector == 'B':
        sector_b +=1
    if sector == 'V':
        sector_v +=1
    if sector == 'G':
        sector_g +=1
percent_a = sector_a / fans * 100
percent_b = sector_b / fans * 100
percent_v = sector_v / fans * 100
percent_g = sector_g / fans * 100
average = fans / capacity * 100
print(f"{percent_a:.2f}%")
print(f"{percent_b:.2f}%")
print(f"{percent_v:.2f}%")
print(f"{percent_g:.2f}%")
print(f"{average:.2f}%")