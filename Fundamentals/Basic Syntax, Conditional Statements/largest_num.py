from sys import maxsize
i = 0
num = int(input())
biggest_num = num
for i in range(2):
    num_two = int(input())
    if num_two > biggest_num:
        biggest_num = num_two
    i +=1
print(biggest_num)