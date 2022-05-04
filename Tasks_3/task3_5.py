# 5)Для каждого четного по номеру элемента списка A найти
# его сумму со следующим элементом и записать эти суммы в новый список B.
from Tasks_3.task3_for_all import numlist

numlist_B = []
sum = 0

for i in range(1, len(numlist)-1):
    if i % 2 == 0:
        sum = numlist[i] + numlist[i + 1]
        numlist_B.append(sum)
print(numlist_B)
