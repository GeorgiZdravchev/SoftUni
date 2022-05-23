number = int(input())
n = 0
for i in range(0, number + 1):
    for j in range(0, number + 1):
        for k in range(0, number + 1):
            if i + j + k == number:
                n += 1
print(n)