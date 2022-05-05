# Найти номера минимального и максимального элементов первой
# половины списка.

from task3_for_all import numlist

numlist_half = []
min_max_elem_ind = []
for i in range(len(numlist) // 2):
    numlist_half.append(numlist[i])
for i in range(len(numlist_half)):
    if numlist_half[i] == min(numlist_half):
        min_max_elem_ind.append(i)
    elif numlist_half[i] == max(numlist_half):
        min_max_elem_ind.append(i)
print(f'первая половина списка {numlist_half}')
min_max_elem_ind.reverse()
print(f'номера (индексы )минимального и максимального элементов '
      f'первой половины списка соответственно {min_max_elem_ind}')


