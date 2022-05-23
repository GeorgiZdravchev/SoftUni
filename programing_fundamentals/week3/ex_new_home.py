# цвете	                Роза Далия	Лале	Нарцис	Гладиола
# Цена на брой в лева	5	3.80	2.80	3	      2.50
flower_type = input()
number_of_flowers = int(input())
budget = int(input())
price = 0
if flower_type == "Roses":
    price = number_of_flowers * 5
    if number_of_flowers > 80:
        price -= price * 0.1
elif flower_type == "Dahlias":
    price = number_of_flowers * 3.8
    if number_of_flowers > 90:
        price -= price * 0.15
elif flower_type == "Tulips":
    price = number_of_flowers * 2.8
    if number_of_flowers > 80:
        price -= price * 0.15
elif flower_type == "Narcissus":
    price = number_of_flowers * 3
    if number_of_flowers < 120:
        price += price * 0.15
elif flower_type == "Gladiolus":
    price = number_of_flowers * 2.5
    if number_of_flowers < 80:
        price += price * 0.2
diff = abs(budget - price)
if budget >= price:
    print(f"Hey, you have a great garden with {number_of_flowers} {flower_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
