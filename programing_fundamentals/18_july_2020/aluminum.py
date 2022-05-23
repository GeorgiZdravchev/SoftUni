woodwork = int(input())
type = input()
delivery = input()
price = 0
condition = True
if woodwork < 10:
    print("Invalid order")
    condition = False
if type == '90X130':
    price = 110 * woodwork
    if 30 < woodwork <= 60:
        price -= price * 0.05
    elif 60 < woodwork:
        price -= price * 0.08
elif type == '100X150':
    price = 140 * woodwork
    if 40 < woodwork <= 80:
        price -= price * 0.06
    elif 80 < woodwork:
        price -= price * 0.1
elif type == '130X180':
    price = 190 * woodwork
    if 20 < woodwork <= 50:
        price -= price * 0.07
    elif 50 < woodwork:
        price -= price * 0.12
elif type == '200X300':
    price = 250 * woodwork
    if 25 < woodwork <= 50:
        price -= price * 0.09
    elif 50 < woodwork:
        price -= price * 0.14
if delivery == "With delivery":
    price += 60
if woodwork > 99:
    price -= price * 0.04
if condition:
    print(f"{price:.2f} BGN")


