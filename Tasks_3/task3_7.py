# Удалить из списка все элементы, совпадающие с его минимальным значением.
from Tasks_3.task3_for_all import numlist

n = min(numlist)
print(f'минимальное значение  {n}')
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
