season = input()
kilometers = float(input())
salary = 0
profit = 0
if kilometers <= 5000:
    if season in "Spring Autumn":
        salary = kilometers * 0.75 * 4
    elif season == "Summer":
        salary = kilometers * 0.9 * 4
    elif season == "Winter":
        salary = kilometers * 1.05 * 4
elif 5000 < kilometers <= 10000:
    if season in "Spring Autumn":
        salary = kilometers * 0.95 * 4
    elif season == "Summer":
        salary = kilometers * 1.1 * 4
    elif season == "Winter":
        salary = kilometers * 1.25 * 4
elif 10000 < kilometers <= 20000:
    salary = kilometers * 1.45 * 4
profit = salary - salary * 0.1
print(f"{profit:.2f}")

