budget = int(input())
inp = input()
condition = True
while inp != "End":

    expense = int(inp)
    budget -= expense
    if budget < 0:
        print("You went in overdraft!")
        condition = False
        break
    inp = input()
if condition:
    print("You bought everything needed.")