temperature = float(input())
if temperature >=26 and temperature <=35:
    print("Hot")
elif temperature >=20.1 and temperature <=25.9:
    print("Warm")
elif temperature >=15 and temperature <=20:
    print("Mild")
elif temperature >=12 and temperature <=14.9:
    print("Cool")
elif temperature >=5 and temperature <=11.9:
    print("Cold")
else:
    print("unknown")