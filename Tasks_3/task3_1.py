# Удалить элемент с введенным номером a.


from Tasks_3.task3_for_all import numlist


for i in range(len(numlist)):
   print(f'номер (индекс) элемента со значением {numlist[i]} равен {i}')
print('\n')
del_el = int(input('введите индекс элемента для удаления :  '))
del_el_value = numlist[del_el]
numlist.pop(del_el)
print(f'удален элемент с индексои {del_el} и значением {del_el_value}')
print('список после удаления элемента ')
print(numlist)
