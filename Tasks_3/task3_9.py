# Найти среднее арифметическое элементов списка.
from Tasks_3.task3_for_all import numlist

sum = 0
for i in range(len(numlist)):
    sum += numlist[i]
print(f'среднее арифметическое элементов списка равно ({sum/len(numlist)})')

