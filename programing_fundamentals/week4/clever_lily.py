age = int(input())
price_washing_machine = float(input())
price_for_toy = int(input())
saved_money = 0
toys = 0
actual_money = 0
for i in range(1, age + 1):
    if i % 2 == 0:
        saved_money += 10 * (i / 2) - 1
    else:
        toys += 1
actual_money = saved_money + toys * price_for_toy
diff = abs(price_washing_machine - actual_money)
if price_washing_machine <= actual_money:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")


