weights = int(input())
price = 0
percent_microbus = 0
percent_truck = 0
percent_train = 0
price_with_microbus = 0
price_with_truck = 0
price_with_train = 0
all_tons = 0
tons_with_microbus = 0
tons_with_truck = 0
tons_with_train = 0
for i in range(1, weights + 1):
    tons = int(input())
    if tons < 4:
        price_with_microbus = tons * 200 + price_with_microbus
        tons_with_microbus = tons + tons_with_microbus
    elif 4 <= tons <= 11:
        price_with_truck = tons * 175 + price_with_truck
        tons_with_truck = tons + tons_with_truck
    else:
        price_with_train = tons * 120 + price_with_train
        tons_with_train = tons + tons_with_train
    all_tons = tons_with_microbus + tons_with_train + tons_with_truck
price = (price_with_microbus + price_with_train + price_with_truck) / all_tons
percent_microbus = tons_with_microbus / all_tons * 100
percent_truck = tons_with_truck / all_tons * 100
percent_train = tons_with_train / all_tons * 100
print(f"{price:.2f}")
print(f"{percent_microbus:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")