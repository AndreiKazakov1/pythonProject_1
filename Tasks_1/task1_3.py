# Даны три числа a, b и c. Найти среднее геометрическое этих
# чисел, если все они отличны от нуля, и среднее арифметическое в противном случае.
import numpy as np

arithmMean = 0
geomMean = 1
condition = False
numList = np.random.randint(0, 10, 3)
print(numList)
for i in range(3):
    arithmMean += numList[i]
    geomMean *= numList[i]
    if numList[i] == 0:
        condition = True
#print(arithmMean)
#print(geomMean)
if condition:
    arithmMean = arithmMean / len(numList)
    print(f'среднее арифметическое : {arithmMean}')
else:
    geomMean = pow(geomMean, 1 / len(numList))
    print(f'среднее геометрическое :{geomMean}')
