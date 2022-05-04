# Найти среднее арифметическое трех последних элементов списка.

from task3_for_all import numlist

sum_last3_elem = 0
#numlist.reverse()
print(numlist)
for i in range(3):
    sum_last3_elem += numlist[i]
print(f'среднее арифметическое трех последних элементов списка  {sum_last3_elem / 3}')
