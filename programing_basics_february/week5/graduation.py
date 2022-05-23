name = input()
inpt = float(input())
avg_grade = 0
bad_grade = 0
grades = 1
clas = 1
while grades <= 12:
    grade = float(inpt)
    if grade >= 4:
        avg_grade += grade
        clas += 1
        grades += 1
    elif grade < 4:
        bad_grade += 1
    if bad_grade > 1:
        break
    if clas == 13:
        break
    inpt = float(input())
if clas == 13 :
    print(f"{name} graduated. Average grade: {avg_grade / 12:.2f}")
if bad_grade > 1:
    print(f"{name} has been excluded at {clas} grade")