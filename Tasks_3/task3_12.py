# Найти номер минимального элемента списка.

from task3_for_all import numlist

index_min_elem = []
for i in range(len(numlist)):
    if numlist[i] == min(numlist):
        index_min_elem.append(i)
print(f' значение минимального элемента списка = {min(numlist)}')
print(f' индекс(сы) минимального(х) элемента(тов) списка  - {index_min_elem}')



