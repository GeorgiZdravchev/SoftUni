student = 0
standard = 0
kid = 0
total_tickets = 0
condition = True
while True:
    name = input()
    if name == "Finish":
        condition = False
        break
    free_space = int(input())
    i = 1
    taken_space = 0
    while i <= free_space:
        type = input()
        i += 1
        if type == "End":
            break
        elif type == "student":
            student += 1
        elif type == "standard":
            standard += 1
        elif type == "kid":
            kid += 1
        taken_space += 1
        total_tickets += 1
    print(f"{name} - {taken_space / free_space * 100:.2f}% full.")
if not condition:
    print(f"Total tickets: {total_tickets}")
    print(f"{student / total_tickets * 100:.2f}% student tickets.")
    print(f"{standard / total_tickets * 100:.2f}% standard tickets.")
    print(f"{kid / total_tickets * 100:.2f}% kids tickets.")

