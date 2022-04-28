# Ввести три числа m, n, p. Подсчитать количество отрицательных чисел.
# МОЖНО ВВЕСТИ ЛЮБОЕ КОЛ-ВО ЧИСЕЛ ОТ -10 ДО 10

import numpy as np
import random

qty = 0
num = int(input("insert any quantity of numbers :\n"))
numList = np.random.randint(-10, 10, num)
print(numList)
# print(len(numList))
for i in range(len(numList)):
    if numList[i] < 0:
        qty += 1
print(f'quantity of negative numbers is: {qty}')

