# Дано натуральное трехзначное число n. Верно ли, что среди его цифр есть 0 или 9?

from random import randint

num = randint(100, 999)
flag_0 = False
flag_9 = False
print(num)
while num != 0:
    x = num % 10
    num //= 10
    if x == 0:
        flag_0 = True
    if x == 9:
        flag_9 = True
if flag_0:
    print('среди цифр числа есть 0')
if flag_9:
    print('среди цифр числа есть 9')


"""
num_1 = randint(100, 999)
y = 0
print(num_1)
while num_1 != 0:
    x = num_1 % 10
    num_1 //= 10
    if x == 0 or x == 9:
        y += 1
if y > 0:
    print('среди цифр числа есть 0 либо 9')
"""