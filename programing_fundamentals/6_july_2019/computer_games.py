sold_games = int(input())
i = 0
hearthstone = 0
fortnite = 0
overwatch = 0
others = 0
hearthstone_percent = 0
fortnite_percent = 0
overwatch_percent = 0
others_percent = 0
while i < sold_games:
    name = input()
    if name == "Hearthstone":
        hearthstone += 1
    elif name == "Fornite":
        fortnite += 1
    elif name == "Overwatch":
        overwatch += 1
    else:
        others += 1
    i += 1
hearthstone_percent = hearthstone / sold_games * 100
fortnite_percent = fortnite / sold_games * 100
overwatch_percent = overwatch / sold_games * 100
others_percent = others / sold_games * 100
print(f"Hearthstone - {hearthstone_percent:.2f}%")
print(f"Fornite - {fortnite_percent:.2f}%")
print(f"Overwatch - {overwatch_percent:.2f}%")
print(f"Others - {others_percent:.2f}%")