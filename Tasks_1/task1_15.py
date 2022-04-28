# Определить есть ли среди заданных целых чисел
# A, B, C, D хотя бы одно чётное.

from random import randint

numlist = [randint(-20, 20) for _ in range(4)]
numdict = {numlist[0]: 'A', numlist[1]: 'B',
           numlist[2]: 'C', numlist[3]: 'D'}
count = 0
print(numlist)
for i in range(len(numlist)):
    if numlist[i] % 2 == 0:
        print(f'среди заданных целых чисел есть четное {numdict.get(numlist[i])}'
              f'  равное {numlist[i]}')
    else:
        count += 1
if count == 4:
    print('среди заданных целых чисел нет четных')

