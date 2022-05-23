n = int(input())
odd_sum = 0
even_sum = 0
for i in range(0, n):
    num = int(input())
    if i % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
diff = abs(even_sum-odd_sum)
if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    print("No")
    print(f"Diff = {diff}")