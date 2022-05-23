turns = int(input())
a = 0
b = 0
c = 0
d = 0
e = 0
invalid = 0
result = 0
percent_a = 0
percent_b = 0
percent_c = 0
percent_d = 0
percent_e = 0
percent_invalid = 0
for i in range(1, turns + 1):
    num = int(input())
    if 0 <= num <= 9 :
        a = a + 1
        result = result + num * 0.2
    if 10 <= num <= 19 :
        b = b + 1
        result = result + num * 0.3
    if 20 <= num <= 29 :
        c = c + 1
        result = result + num * 0.4
    if 30 <= num <= 39 :
        d = d + 1
        result = result + 50
    if 40 <= num <= 50 :
        e = e + 1
        result = result + 100
    if 50 < num or 0 > num:
        invalid = invalid + 1
        result = result / 2
percent_a = a / turns * 100
percent_b = b / turns * 100
percent_c = c / turns * 100
percent_d = d / turns * 100
percent_e = e / turns * 100
percent_invalid = invalid / turns * 100
print(f"{result:.2f}")
print(f"From 0 to 9: {percent_a:.2f}%")
print(f"From 10 to 19: {percent_b:.2f}%")
print(f"From 20 to 29: {percent_c:.2f}%")
print(f"From 30 to 39: {percent_d:.2f}%")
print(f"From 40 to 50: {percent_e:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")
