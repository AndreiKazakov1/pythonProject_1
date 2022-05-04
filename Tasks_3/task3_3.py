# 3) Удалить элементы, индексы которых кратны 7.
from Tasks_3.task3_for_all import numlist


indexlist = []
for i in range(len(numlist)):
    print(f'индекс {i} // значение {numlist[i]} ')
for i in range(1, len(numlist)):
    if i % 7 == 0:
        indexlist.append(i)
        numlist.pop(i)
        numlist.insert(0, 'x')
print(indexlist)
print(numlist)
for i in range(len(numlist)):
    if numlist[i] == 'x':
        numlist.pop(i)
print(numlist)

