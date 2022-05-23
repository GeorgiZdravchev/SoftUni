capacity = float(input())
loaded_suitcases = 0
weight_suitcases = 0
i = 1
while True:
    weight = input()
    if weight == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    weight = float(weight)
    if i % 3 == 0:
        weight += weight * 0.1
    weight_suitcases += weight
    if weight_suitcases >= capacity:
        print("No more space!")
        break
    loaded_suitcases += 1
print(f"Statistic: {loaded_suitcases} suitcases loaded.")

