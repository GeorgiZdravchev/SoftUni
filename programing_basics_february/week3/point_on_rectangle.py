x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())
if x1 < x < x2 and y1 < y < y2:
    print("Inside / Outside")
elif x1 > x > x2 and y1 > y > y2:
    print("Inside / Outside")
elif x1 <= x <= x2 and not y1 < y < y2:
    print("Inside / Outside")
elif x1 < x < x2 and not y1 <= y <= y2:
    print("Inside / Outside")
elif x1 == x or x == x2 or y1 == y or y == y2:
    print("Border")
elif x == x1 or x == x2:
    if y1 >= y <= y2:
        print("Border")
elif y==y1 or y == y2:
     if x1 >= x <= x2:
        print("Border")
else:
    print("Inside / Outside")