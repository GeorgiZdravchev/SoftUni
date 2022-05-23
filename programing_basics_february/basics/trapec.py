side_a = float(input())
side_b = float(input())
hight = float(input())
area = (side_b + side_a) * hight / 2
formatted_float = "{:.2f}".format(area)
print(formatted_float)