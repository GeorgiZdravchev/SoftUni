n = int(input())
condition = False
current = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        if current > n:
            condition = True
            break
        print(str(current) + ' ', end='')
        current += 1
    if condition:
        break
    print()