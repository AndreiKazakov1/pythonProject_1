# Даны три числа a, b, c.
# Значение наибольшего из них присвоить переменной d.

import numpy as np

"""numList = np.random.randint(-100, 100, 3)
a = numList[0]
b = numList[1]
c = numList[2]
d = max(numList)
print(f'даны три числа a = {a}, b= {b}, c= {c}')
print(f'значение наибольшего из них присвоено переменной d и равно  {d}')
"""


# сокращенный вариант

import numpy as np

numList = np.random.randint(-100, 100, 3)
print(f'даны три числа a = {numList[0]}, b= {numList[1]}, c= {numList[2]}')
print(f'значение наибольшего из них присвоено переменной d и равно  {max(numList)}')
