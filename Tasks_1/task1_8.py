# Дано натуральное четырехзначное число n. Верно ли, что все его цифры различны?
from random import randint

num = randint(1000, 9999)
num_arr = []
print(f'натуральное четырехзначное число :{ num}')
while num != 0:
    x = num % 10
    num_arr.append(x)
    num //= 10
num_arr.reverse()
#print(num_arr)
same_num = []
shift = 1
flag = False
for i in range(len(num_arr)):
    for j in range(shift, len(num_arr)):
        if num_arr[i] == num_arr[j]:
            flag = True
            same_num.append(num_arr[i])
    shift = shift + 1
if not flag:
    print("все цифры данного числа различны")
else:
    print(f'в данном числе есть одинаковые цифры : {same_num}')

