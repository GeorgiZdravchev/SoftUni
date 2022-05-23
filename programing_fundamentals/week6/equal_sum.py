num1 = int(input())
num2 = int(input())
for i in range(num1, num2 + 1):
    number_to_str = str(i)
    even_sum = 0
    odd_sum = 0
    for j in range(len(number_to_str)):
        if j % 2 == 0:
            even_sum += int(str(i)[j])
        else:
            odd_sum += int(str(i)[j])
    if even_sum == odd_sum:
        print(i, end=' ')

