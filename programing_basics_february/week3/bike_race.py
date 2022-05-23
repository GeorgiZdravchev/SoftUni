juniors = int(input())
seniors = int(input())
course = input()
tax = 0
if course == "trail":
    tax = 5.5 * juniors + 7 * seniors
if course == "cross-country":
    tax = 8 * juniors + 9.5 * seniors
if course == "downhill":
    tax = 12.25 * juniors + 13.75 * seniors
if course == "road":
    tax = 20 * juniors + 21.5 * seniors
if course == "cross-country" and juniors + seniors >= 50:
    tax -= tax * 0.25
money_left = tax - 0.05 * tax
print(f"{money_left:.2f}")
