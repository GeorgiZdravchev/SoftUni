inpt = input()
books_count = 0
book = ''
statement = True
while book != "No More Books":
    book = input()
    if book != inpt and book != "No More Books":
        books_count += 1
    elif book == inpt:
        print(f"You checked {books_count} books and found it.")
        statement = False
        break
if statement:
    print(f"The book you search is not here!")
    print(f"You checked {books_count} books.")
