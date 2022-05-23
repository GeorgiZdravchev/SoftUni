excursions_sea = int(input())
excursions_mountain = int(input())
profit = 0
condition = False
while True:
    command = input()
    if command == "Stop":
        condition = True
        break
    if command == "sea" and excursions_sea > 0:
        profit += 680
        excursions_sea -= 1
    elif command == 'mountain' and excursions_mountain > 0:
        profit += 499
        excursions_mountain -= 1
    if excursions_mountain == 0 and excursions_sea == 0:
        break
if not condition:
    print(f"Good job! Everything is sold.")
print(f"Profit: {profit} leva.")

