budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25 / 4
whole_price = flour_price + eggs_price + milk_price
colored_eggs = 0
breads_made = 0
while budget > whole_price:
    breads_made += 1
    colored_eggs += 3
    if breads_made % 3 == 0:
        colored_eggs -= breads_made - 2
    budget -= whole_price
print(f"You made {breads_made} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")