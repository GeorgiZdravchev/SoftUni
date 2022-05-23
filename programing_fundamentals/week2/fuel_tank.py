fuel = input()
liters = int(input())
if liters >= 25 :
    if fuel == "Diesel" :
        lower_fuel = fuel.lower()
        print(f"You have enough {lower_fuel}.")
    elif fuel == "Gas" :
        lower_fuel = fuel.lower()
        print(f"You have enough {lower_fuel}.")
    elif fuel == "Gasoline" :
        lower_fuel = fuel.lower()
        print(f"You have enough {lower_fuel}.")
    else:
        print("Invalid fuel!")
else:
    if fuel == "Diesel" :
        lower_fuel = fuel.lower()
        print(f"Fill your tank with {lower_fuel}!")
    elif fuel == "Gas" :
        lower_fuel = fuel.lower()
        print(f"Fill your tank with {lower_fuel}!")
    elif fuel == "Gasoline" :
        lower_fuel = fuel.lower()
        print(f"Fill your tank with {lower_fuel}!")
    else:
        print("Invalid fuel!")

