import math
r = float(input())
calculated_area = math.pi * r * r
calculated_parameter = 2 * math.pi * r
formatted_area = "{:.2f}".format(calculated_area)
formatted_parameter = "{:.2f}".format(calculated_parameter)
print(formatted_area)
print(formatted_parameter)
