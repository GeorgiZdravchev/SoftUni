nailon_needed = int(input())
paint_needed = int(input())
razreditel_needed = int(input())
hours_needed = int(input())
sum_of_nailoon = (nailon_needed + 2) * 1.50
sum_of_paint = (paint_needed + (paint_needed * 0.1)) * 14.50
sum_of_razreditel = razreditel_needed * 5
torbichiki = 0.4
sum_of_materials = sum_of_paint + sum_of_razreditel + sum_of_nailoon + torbichiki
sum_for_workers = sum_of_materials * 0.3 * hours_needed
final_sum = sum_for_workers + sum_of_materials
print(final_sum)