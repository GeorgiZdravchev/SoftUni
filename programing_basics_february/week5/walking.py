steps = 0
inpt = input()
while True:
    if inpt == "Going home":
        bonus_steps = int(input())
        steps += bonus_steps
        break
    else:
        steps += int(inpt)
        if steps >= 10000:
            break
    inpt = input()
diff = abs(steps - 10000)
if steps < 10000:
    print(f"{diff} more steps to reach goal.")
else:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")