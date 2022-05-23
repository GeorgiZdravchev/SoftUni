number1 = int(input())
number2 = int(input())
magic_number = int(input())
combination = 0
condition = False
for i in range(number1, number2 + 1):
    for j in range(number1, number2 + 1):
        combination += 1
        if i + j == magic_number:
            print(f'Combination N:{combination} ({i} + {j} = {magic_number})')
            condition = True
            break
    if condition:
        break
if not condition:
    print(f'{combination} combinations - neither equals {magic_number}')