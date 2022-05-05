# 3) Удалить элементы, индексы которых кратны 7.
from Tasks_3.task3_for_all import numlist

indexlist = []
for i in range(len(numlist)):
    print(f'индекс {i} // значение {numlist[i]} ')
for i in range(1, len(numlist)):
    if i % 7 == 0:
        indexlist.append(i)
        numlist.pop(i)
        numlist.insert(0, -1)
print(f'индексы элементов для удаления  {indexlist}')
# print(numlist)
while -1 in numlist:
    numlist.remove(-1)
print(f'результат после удаления {numlist}')


