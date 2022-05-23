btc = int(input())
yoan = float(input())
commission = float(input())
yoan_in_dollar = yoan * 0.15
dollar_in_lev = yoan_in_dollar * 1.76
levs = btc * 1168 + dollar_in_lev
euro = levs / 1.95
price_after_commission = euro - euro * commission / 100
print(f"{price_after_commission:.2f}")
