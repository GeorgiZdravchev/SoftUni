sum = 0
dgh = input()
while dgh != "NoMoreMoney":
    money = float(dgh)
    if money < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {money:.2f}")
    sum += money
    dgh = input()
print(f"Total: {sum:.2f}")
# inpt = input()
#
# balance = 0.0
#
# while inpt != "NoMoreMoney":
#
#     amount = float(inpt)
#
#     if amount < 0:
#         print("Invalid operation!")
#         break
#     balance += amount
#
#     print(f"Increase: {amount:.2f}")
#
#     inpt = input()
#
# print(f"Total: {balance:.2f}")