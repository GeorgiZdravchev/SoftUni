n1 = int(input())
n2 = int(input())
operator = input()
result = 0
type_of_number = ''
left = 0
statement = True
if operator == "+":
    result = n1 + n2
    if result % 2 == 0:
        type_of_number = "even"
    else:
        type_of_number = "odd"
elif operator == "-":
    result = n1 - n2
    if result % 2 == 0:
        type_of_number = "even"
    else:
        type_of_number = "odd"
elif operator == "*":
    result = n1 * n2
    if result % 2 == 0:
        type_of_number = "even"
    else:
        type_of_number = "odd"
elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
        statement = False
    else:
        result = n1 / n2

elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
        statement = False
    else:
        left = n1 % n2

if operator in "+ - *":
    print(f"{n1} {operator} {n2} = {result} - {type_of_number}")
elif operator == "/":
    if statement:
        print(f"{n1} / {n2} = {result:.2f}")
elif operator == "%":
    if statement:
        print(f"{n1} % {n2} = {left}")

