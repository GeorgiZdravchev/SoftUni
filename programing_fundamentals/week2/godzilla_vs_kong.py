budget = float(input())
statist = int(input())
price_of_clothing = float(input())
price_of_decor = 0.1 * budget
sum_of_clothing = statist * price_of_clothing

if statist >= 150 :
    sum_of_clothing -= sum_of_clothing * 0.1
price_of_movie = sum_of_clothing + price_of_decor
diff = abs(budget - price_of_movie)
formatted_diff = "{:.2f}".format(diff)
if  price_of_movie > budget :
    print("Not enough money!")
    print(f"Wingard needs {formatted_diff} leva more.")
else :
    print("Action!")
    print(f"Wingard starts filming with {formatted_diff} leva left.")
