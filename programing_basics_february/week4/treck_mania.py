groups = int(input())
p_musala = 0
p_monblan = 0
p_kilimandjaro = 0
p_k2 = 0
p_everest = 0
sum_people = 0
for i in range(1, groups + 1):
    people = int(input())
    if people <= 5:
        p_musala += people
    elif 6 <= people <= 12:
        p_monblan += people
    elif 13 <= people <= 25:
        p_kilimandjaro += people
    elif 26 <= people <= 40:
        p_k2 += people
    elif 41 <= people:
        p_everest += people
    sum_people += people
print(f"{p_musala / sum_people * 100:.2f}%")
print(f"{p_monblan / sum_people * 100:.2f}%")
print(f"{p_kilimandjaro / sum_people * 100:.2f}%")
print(f"{p_k2 / sum_people * 100:.2f}%")
print(f"{p_everest / sum_people * 100:.2f}%")