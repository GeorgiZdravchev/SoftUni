price_for_the_year = int(input())
shoes = price_for_the_year - 0.40 * price_for_the_year
kit = shoes - 0.2 * shoes
ball = kit * 0.25
accesories = 0.2 * ball
price_for_all = price_for_the_year + shoes +kit + ball + accesories
print(price_for_all)