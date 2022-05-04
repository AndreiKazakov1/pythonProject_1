# 2) Все четные по значению элементы исходного списка A поместить в новый список B.

from Tasks_3.task3_for_all import numlist

numlist_B = []
for i in range(len(numlist)):
	if numlist[i] % 2 == 0:
		numlist_B.append(numlist[i])
numlist_B.reverse()
print(f'новый список {numlist_B}')

