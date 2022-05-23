number_tabs = int(input())
salary = float(input())
for i in range(number_tabs):
    tab = input()
    if tab == "Facebook":
        salary -= 150
    elif tab == "Instagram":
        salary -= 100
    elif tab == "Reddit":
        salary -= 50
    if salary <= 0:
        break
if salary <= 0:
    print("You have lost your salary.")
else:
    print(int(salary))