budget = float(input())
video_card = int(input())
processor = int(input())
ram = int(input())
# •	Видеокарта – 250 лв./бр.
# •	Процесор – 35% от цената на закупените видеокарти/бр.
# •	Рам памет – 10% от цената на закупените видеокарти/бр.
video_card_price = video_card * 250
processor_price = video_card_price * 0.35
ram_price = video_card_price * 0.1
total = video_card_price + processor_price * processor + ram_price * ram
if video_card > processor:
    total -= total * 0.15
diff = abs(budget - total)
formatted_diff = "{:.2f}".format(diff)
if total <= budget :
    print(f"You have {formatted_diff} leva left!")
else :
    print(f"Not enough money! You need {formatted_diff} leva more!")

