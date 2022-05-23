orders = int(input())
total_price = 0
price_for_the_day = 0
for i in range(orders):
    ppc = float(input())
    days = int(input())
    capsules = int(input())
    if ppc < 0.01 or ppc > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules < 1 or capsules > 2000:
        continue
    price_for_the_day = ppc * days * capsules
    total_price += price_for_the_day
    print(f"The price for the coffee is: ${price_for_the_day:.2f}")
print(f"Total: ${total_price:.2f}")

