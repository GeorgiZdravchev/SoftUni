trip_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())
#  Пъзел - 2.60 лв.
#  Говореща кукла - 3 лв.
#  Плюшено мече - 4.10 лв.
#  Миньон - 8.20 лв.
#  Камионче - 2 лв.
sum = puzzles * 2.6 + dolls * 3 + bears * 4.1 + minions * 8.2 + trucks * 2
if puzzles + dolls + bears + minions + trucks >= 50 :
    sum -= sum * 0.25
    loan = sum * 0.1
    winnings = sum - loan
    money_left = abs(winnings - trip_price)
    formatted_money = "{:.2f}".format(money_left)
    if winnings >= trip_price :
        print(f"Yes! {formatted_money} lv left.")
    else :
        print(f"Not enough money! {formatted_money} lv needed.")
else :
    loan = sum * 0.1
    winnings = sum - loan
    money_left = abs(winnings - trip_price)
    formatted_money = "{:.2f}".format(money_left)
    if winnings >= trip_price:
        print(f"Yes! {formatted_money} lv. left")
    else:
        print(f"Not enough money! {formatted_money} lv needed.")
