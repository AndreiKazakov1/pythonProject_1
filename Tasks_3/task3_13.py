# Найти для каждого элемента списка А сумму предыдущих
# элементов и записать эти суммы в новый список B.

from task3_for_all import numlist

sum_list = []
sum = 0
for i in range(len(numlist)):
    if i == 0:
        sum_list.append('нет суммы предыдущих элементов')
        print(f'для {i+1} - го  элемента списка А равного {numlist[0]}  {sum_list[0]}')
    else:
        sum += numlist[i-1]
        sum_list.append(sum)
        print(f'для {i+1} - го   элемента списка А равного {numlist[i]} сумма предыдущих элементов равна {sum}')
print(f'список сумм  {sum_list}')


