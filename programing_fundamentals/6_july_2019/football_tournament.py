name = input()
games = int(input())
i = 0
w = 0
d = 0
l = 0
points = 0
condition = True
while i < games:
    result = input()
    if result == "W":
        w += 1
    elif result == "D":
        d += 1
    elif result == "L":
        l += 1
    i += 1
points = w * 3 + d
if games == 0:
    print(f"{name} hasn't played any games during this season.")

if games >= 1:
    win_rate = w / games * 100
    print(f"{name} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {w}")
    print(f"## D: {d}")
    print(f"## L: {l}")
    print(f"Win rate: {win_rate:.2f}%")

