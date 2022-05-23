lines = int(input())
for i in range(lines):
    word = input()
    for j in range(len(word)):
        letter = word[j]
        if ord(letter) == 44 or ord(letter) == 46 or ord(letter) == 95:
            print(f"{word} is not pure!")
            break
    else:
        print(f"{word} is pure.")