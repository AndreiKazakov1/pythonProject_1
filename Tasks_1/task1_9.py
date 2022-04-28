# Проверить, является ли дробь A / B правильной.

from random import randint

numerator = randint(-9, 9)
denomerator = randint(-9, 9)
fraction = numerator/denomerator
result = ''
if abs(numerator) >= abs(denomerator):
    result = 'improper fraction'
elif abs(numerator) < abs(denomerator):
    result = 'proper fraction'
print(f'fraction {numerator}/{denomerator} is {result} (= {fraction})')
