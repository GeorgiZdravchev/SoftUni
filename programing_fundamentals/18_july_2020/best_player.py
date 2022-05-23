import sys
from sys import maxsize
max = -sys.maxsize
best_player = ''
while True:
    name = input()
    if name == "END":
        break
    goals = int(input())
    if goals > max:
        max = goals
        best_player = name
    if max >= 10:
        break
print(f"{best_player} is the best player!")
if max >= 3:
    print(f"He has scored {max} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max} goals.")

