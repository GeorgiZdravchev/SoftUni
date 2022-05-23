width = int(input())
length = int(input())
pieces = width * length
pieces_taken = 0
while True:
    inpt = input()
    if inpt == "STOP":
        break
    pieces_taken += int(inpt)
    if pieces < pieces_taken:
        break
diff = abs(pieces - pieces_taken)
if pieces_taken < pieces:
    print(f"{diff} pieces are left.")
else:
    print(f"No more cake left! You need {diff} pieces more.")