word_to_double = ''
word = ''
while word_to_double != "End":
    prnt = ''
    word = input()
    if word == "End":
        break
    word_to_double = str(word)
    if word_to_double == "SoftUni":
        continue
    for i in range(len(word_to_double)):
        prnt += word_to_double[i]
        prnt += word_to_double[i]
    print(prnt)


