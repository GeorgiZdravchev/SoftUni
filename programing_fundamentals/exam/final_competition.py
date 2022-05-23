dancers = int(input())
points = float(input())
season = input()
place = input()
money_won = 0
if place == "Bulgaria":
    money_won = dancers * points
    if season == "summer":
        money_won -= money_won * 0.05
    elif season == "winter":
        money_won -= money_won * 0.08
elif place == "Abroad":
    money_won = dancers * points
    money_won += money_won * 0.5
    if season == "summer":
        money_won -= money_won * 0.1
    elif season == "winter":
        money_won -= money_won * 0.15
charity = money_won * 0.75
money_won -= charity
money_per_dancer = money_won / dancers
print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")