divisor = int(input())
boundary = int(input())
biggest_number = 0
for i in range (divisor, boundary +1):
    if i % divisor == 0:
        biggest_number = i
    i += 1
print(biggest_number)