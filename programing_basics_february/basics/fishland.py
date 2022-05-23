skumriya_price = float(input())
caca_price = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = int(input())
palamud_price = (skumriya_price + skumriya_price * 0.60) * kg_palamud
safrid_price = (caca_price + caca_price * 0.80) * kg_safrid
midi_price = kg_midi * 7.5
full_price = safrid_price + palamud_price + midi_price
formatted_price = "{:.2f}".format(full_price)
print(formatted_price)