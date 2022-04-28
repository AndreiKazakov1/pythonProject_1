# Определить, имеется ли среди трёх чисел a, b и c хотя бы
# одна пара равных между собой чисел.

import random

answer = ""
numList = [random.randint(0, 10) for _ in range(3)]
print(numList)
for i in range(3):
    if numList[0] == numList[1] or numList[0] == numList[2] or numList[1] == numList[2]:
        answer = 'тут есть хотя бы одна пара равных между собой чисел'
    else:
        answer = 'тут нет равных между собой чисел'
print(answer)
