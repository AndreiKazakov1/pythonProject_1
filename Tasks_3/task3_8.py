# Найти значение максимального элемента списка.
from Tasks_3.task3_for_all import numlist

print(f'максимальное значение в списке равно  {max(numlist)}')
count = 0
for i in range(len(numlist)):
    if numlist[i] == max(numlist):
        count += 1
print(f'количество максимальных элементов в списке равно  {count}')
