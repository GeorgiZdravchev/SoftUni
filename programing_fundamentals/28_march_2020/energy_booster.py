fruit = input()
size = input()
orders = int(input())
price = 0
price_with_discount = 0
if size == 'small':
    if fruit == "Watermelon":
        price = 2 * 56 * orders
    elif fruit == "Mango":
        price = 2 * 36.66 * orders
    elif fruit == "Pineapple":
        price = 2 * 42.1 * orders
    elif fruit == "Raspberry":
        price = 2 * 20 * orders
elif size == 'big':
    if fruit == "Watermelon":
        price = 5 * 28.7 * orders
    elif fruit == "Mango":
        price = 5 * 19.6 * orders
    elif fruit == "Pineapple":
        price = 5 * 24.8 * orders
    elif fruit == "Raspberry":
        price = 5 * 15.2 * orders
if 400 <= price <= 1000:
    price -= price * 0.15
elif 1000 <  price:
    price -= price * 0.5
print(f"{price:.2f} lv.")