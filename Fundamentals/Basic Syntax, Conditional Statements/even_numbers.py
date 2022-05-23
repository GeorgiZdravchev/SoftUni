number_of_numbers = int(input())
condition = True
for i in range (0, number_of_numbers):
    num = int(input())
    if num % 2 != 0:
        print(f"{num} is odd!")
        condition = False
        break
if condition:
    print("All numbers are even.")

