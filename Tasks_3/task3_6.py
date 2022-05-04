# Удалить все элементы с заданным значением, если они имеются в списке.
from Tasks_3.task3_for_all import numlist

n = int(input('введите значение для удаления :'))
count = 0
numlist_len = len(numlist)
for i in range(len(numlist)):
    if numlist[i] == n:
        break
    else:
        count += 1
if count == len(numlist):
    print('нет такого элемента для удаления')
while n in numlist:
    numlist.remove(n)
if numlist_len > len(numlist):
    print(f'результат  {numlist}')
