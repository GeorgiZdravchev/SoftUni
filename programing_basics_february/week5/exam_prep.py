bad_grades = int(input())
avg_grades = 0
exercises = 0
bad_grade = 0
last_name = ''
condition = True
while bad_grade < bad_grades:
    name = input()
    if name == "Enough":
        condition = False
        break
    grade = int(input())
    if grade <= 4:
        bad_grade += 1
    exercises += 1
    avg_grades += grade
    last_name = name
if not condition:
    print(f"Average score: {avg_grades / exercises:.2f}")
    print(f"Number of problems: {exercises}")
    print(f"Last problem: {last_name}")
if condition:
    print(f"You need a break, {bad_grades} poor grades.")