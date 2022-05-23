command = input()
coffees = 0
while command != "END":
    if command in('coding', 'dog', 'cat', 'movie'):
        coffees += 1
    elif command in('CODING', 'CAT', 'DOG', 'MOVIE'):
        coffees += 2
    command = input()
if coffees <= 5:
    print(coffees)
else:
    print('You need extra sleep')