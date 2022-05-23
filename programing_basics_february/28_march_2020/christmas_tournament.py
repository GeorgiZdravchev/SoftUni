days = int(input())
total_wins = 0
total_loses = 0
total_income = 0
for i in range(days):
    wins_for_day = 0
    loses_for_day = 0
    while True:
        sport = input()
        income = 0
        if sport == "Finish":
            break
        result = input()
        if result == "win":
            total_wins += 1
            wins_for_day += 1
            income += 20
        elif result == "lose":
            total_loses += 1
            loses_for_day += 1
        if wins_for_day > loses_for_day:
            income += income * 0.1
        total_income += income
if total_wins > total_loses:
    total_income += total_income * 0.2
    print(f"You won the tournament! Total raised money: {total_income:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_income:.2f}")


