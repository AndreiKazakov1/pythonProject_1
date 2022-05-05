# Найти индексы первого и последнего нулевых элементов списка.

from task3_for_all import numlist

try:
    index_list = []
    for i in range(len(numlist)):
        print(f'индекс {i} // значение {numlist[i]} ')
        if numlist[i] == 0:
            index_list.append(i)
    print(index_list)
    print(f'индекс первого нулевого элемента списка {min(index_list)}')
    if max(index_list) != min(index_list):
        print(f'индекс последнего нулевого элемента списка {max(index_list)}')
except Exception:
    print('в списке нет нулевых элементов')
