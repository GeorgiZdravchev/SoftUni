students = int(input())
f = 0
d = 0
c = 0
b = 0
percent_f = 0
percent_d = 0
percent_c = 0
percent_b = 0
sum_grades = 0
for i in range(1, students + 1):
    grade = float(input())
    if grade <= 2.99:
        f = f + 1
    if 3 <= grade <= 3.99:
        d = d + 1
    if 4 <= grade <= 4.99:
        c += 1
    if 5 <= grade:
        b += 1
    sum_grades += grade
    average = sum_grades / students
percent_b = b / students * 100
percent_c = c / students * 100
percent_d = d / students * 100
percent_f = f / students * 100
print(f'Top students: {percent_b:.2f}%')
print(f'Between 4.00 and 4.99: {percent_c:.2f}%')
print(f'Between 3.00 and 3.99: {percent_d:.2f}%')
print(f'Fail: {percent_f:.2f}%')
print(f"Average: {average:.2f}")