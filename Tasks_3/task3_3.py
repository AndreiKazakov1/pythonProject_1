# 3) Удалить элементы, индексы которых кратны 7.
from Tasks_3.task3_for_all import numlist



for i in range(len(numlist)):
    print(f'индекс {i} // значение {numlist[i]} ')
for i in range(1, len(numlist)):
    if i % 7 == 0:
        numlist.pop(i)
print(numlist)





