num = float(input())
if num == 0:
    print("zero")
elif -1 < num < 1:
    if num < 0:
        print("small negative")
    else:
        print("small positive")
elif -1000 <= num <= 1000:
    if num < 0:
        print("negative")
    else:
        print("positive")
else:
    if num < 0:
        print("large negative")
    else:
        print("large positive")