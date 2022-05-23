jury = int(input())
final_grade = 0
presentations = 0
while True:
    presentation = input()
    current_grade = 0
    if presentation == 'Finish':
        final_grade = final_grade / (jury * presentations)
        print(f"Student's final assessment is {final_grade:.2f}.")
        break
    presentations += 1
    for grade in range(0, jury):
        grades = float(input())
        current_grade += grades
    final_grade += current_grade
    current_grade /= jury
    print(f'{presentation} - {current_grade:.2f}.')