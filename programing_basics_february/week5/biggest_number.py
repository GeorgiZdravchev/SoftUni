import sys
inpt = input()
max_num = sys.maxsize
while inpt != "Stop":
    maxnum = int(inpt)
    if maxnum < max_num:
        max_num = maxnum
    inpt = input()
print(max_num)