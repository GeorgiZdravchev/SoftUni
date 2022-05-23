primary = 0
non_primary = 0
condition = False
while True:
    number = input()
    if number == "stop":
        break
    number = int(number)
    if number < 0:
        print('Number is negative.')
    else:
        for i in range(2, number):
            if number % i == 0:
                condition = True
                break
        if condition:
            non_primary += number
            condition = False
        else:
            primary += number
print(f'Sum of all prime numbers is: {primary}')
print(f'Sum of all non prime numbers is: {non_primary}')
