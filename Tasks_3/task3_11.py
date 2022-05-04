# Удалить пять первых нечетных по значению элементов списка.

from task3_for_all import numlist

count = 0
i = 0
while i < len(numlist):
    if numlist[i] % 2 != 0 and count < 5:
        del numlist[i]
        count += 1
    else:
        i += 1
print(f'result is  {numlist}')
